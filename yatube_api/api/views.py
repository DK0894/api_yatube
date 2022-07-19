from django.shortcuts import get_object_or_404
from rest_framework import mixins, permissions, viewsets

from posts.models import Group, Post

from .permissions import IsAuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ListRetrieveViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                          viewsets.GenericViewSet):
    pass


class GroupViewSet(ListRetrieveViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated, IsAuthorOrReadOnly,)

    @staticmethod
    def __get_post(kwargs):
        return get_object_or_404(Post, pk=kwargs.get('post_id'))

    def get_queryset(self):
        return self.__get_post(self.kwargs).comments.all()

    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post=self.__get_post(self.kwargs)
        )
