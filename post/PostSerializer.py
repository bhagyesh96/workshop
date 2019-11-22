from rest_framework import serializers
from .models import Post,PostDetail

class PostDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostDetail
        fields = '__all__'
        

class PostSerializer(serializers.ModelSerializer):
    pd = PostDetailSerializer(many=True)
    class Meta:
        model = Post
        fields = ['id', 'likes','title', 'text','cover','pd']

class PostCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'likes', 'text','cover','title']