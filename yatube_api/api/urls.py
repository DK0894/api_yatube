from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

app_name = 'api'


router = DefaultRouter()
router.register(r'api/v1/posts', PostViewSet, basename='posts')
router.register(
    r'^api/v1/posts/(?P<post_id>\d+)$', PostViewSet, basename='post')
router.register(r'api/v1/groups', GroupViewSet, basename='groups')
router.register(
    r'^api/v1/groups/(?P<group_id>\d+)$', GroupViewSet,
    basename='group'
)
router.register(
    r'^api/v1/posts/(?P<post_id>\d+)$/comments', CommentViewSet,
    basename='comments'
)
router.register(
    r'^api/v1/posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)$',
    CommentViewSet, basename='comment'
)


urlpatterns = [
    path('', include(router.urls)),
    path('api/v1/api-token-auth/', include('djoser.urls')),
    path('api/v1/api-token-auth/', include('djoser.urls.jwt')),
]