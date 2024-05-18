from django.shortcuts import render
# Create your views here.
from  rest_framework import viewsets # type: ignore
from .models import Article
from .serializers import ArticleSerializer

class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    