from rest_framework.viewsets import ModelViewSet
from categories.api.serializers import CategorySerializer
from categories.models import Category
from categories.api.permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CategoryApiViewSet(ModelViewSet):
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    # queryset = Category.objects.filter(published=True)  # esto filtra para TODAS las request que usen esta View
    lookup_field = 'slug'  # toma el lugar de /id y se puede usar cualquier campo unique
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['title', 'id']



