from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentsViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(
    r'^posts/(?P<post_id>\d+)$', PostViewSet, basename='post')
router.register(r'groups', GroupViewSet, basename='groups')
router.register(
    r'^groups/(?P<group_id>\d+)$', GroupViewSet,
    basename='group'
)
router.register(
    r'posts/(?P<post_id>\d+)/comments', CommentsViewSet,
    basename='comments'
)
router.register(
    r'posts/(?P<post_id>\d+)/comments/(?P<comment_id>\d+)',
    CommentsViewSet, basename='comment'
)


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
