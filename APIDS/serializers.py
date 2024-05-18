from rest_framework import serializers  # type: ignore
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    class Meta: #class Meta is used to define the fields that we want to expose to the API
        model = Article
        fields = '__all__'
        
