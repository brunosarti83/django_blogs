from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from posts.models import Post
from posts.api.serializers import PostSerializer
from posts.api.permissions import IsAdminOrReadOnly


class PostApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(published=True)
    lookup_field = 'slug'
    filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['category']
    # esto buscaría por id de category, debajo vamos a hacer que filtre por el campo de category que
    # querramos, pero hay que hacer la busqueda como /?category__slug=<slug>... se pueden incluir ambos
    filterset_fields = ['category__slug']



