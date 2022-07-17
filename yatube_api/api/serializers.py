from rest_framework import serializers

from posts.models import Comment, Group, Post, User


class PostSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(
        read_only=True, default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')

        # validators = [
        #     serializers.UniqueTogetherValidator(
        #         queryset=Post.objects.all(),
        #         fields=('author', 'group')
        #     )
        # ]


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    # author = serializers.PrimaryKeyRelatedField(
    #     read_only=True, default=serializers.CurrentUserDefault()
    # )
    # post = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )
    print(author)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
