from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserSerializer
from categories.api.serializers import CategorySerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()  # para que muestre todos los datos de user en lugar de solo id
    category = CategorySerializer()  # para que  muestre toda la info de Category

    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'miniature', 'created_at', 'published', 'user', 'category']

