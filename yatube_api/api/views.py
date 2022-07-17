from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied

from posts.models import Comment, Group, Post, User

from .serializers import CommentSerializer, GroupSerializer, PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужих данных запрещено!')
        super(PostViewSet, self).perform_destroy(instance)


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    @staticmethod
    def __get_post(kwargs):
        print(get_object_or_404(Post, pk=kwargs.get('post_id')))
        return get_object_or_404(Post, pk=kwargs.get('post_id'))

    def get_queryset(self):
        return self.__get_post(self.kwargs).comments

    def perform_create(self, serializer):
        print(serializer.save(
            author=self.request.user,
            post=self.__get_post(self.kwargs)
        ))
        serializer.save(
            author=self.request.user,
            post=self.__get_post(self.kwargs)
        )

    # def get_queryset(self):
    #     post_id = self.kwargs.get('post_id')
    #     get_object_or_404(Post, pk=post_id)
    #     return Comment.objects.filter(post=post_id)
    #
    # def perform_create(self, serializer):
    #     post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
    #     serializer.save(author=self.request.user, post=post)

    # def perform_update(self, serializer):
    #     if serializer.instance.author != self.request.user:
    #         raise PermissionDenied('Изменение чужого контента запрещено!')
    #     super(CommentViewSet, self).perform_update(serializer)
    #
    # def perform_destroy(self, instance):
    #     if instance.author != self.request.user:
    #         raise PermissionDenied('Удаление чужих данных запрещено!')
    #     super(CommentViewSet, self).perform_destroy(instance)
