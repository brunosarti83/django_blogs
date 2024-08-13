from posts.api.views import PostApiViewSet
from rest_framework.routers import DefaultRouter

router_posts = DefaultRouter()

router_posts.register(prefix='posts', basename='posts', viewset=PostApiViewSet)

