from django.shortcuts import render
from rest_framework import generics, serializers
from .serializers import HighlightedTextSerializer
from .models import Snippets
# Create your views here.

class SnippetList(generics.ListAPIView):
    queryset = Snippets.objects.all()
    serializer_class = HighlightedTextSerializer

class GetSnippet(generics.RetrieveAPIView):
    queryset = Snippets.objects.all()
    serializer_class = HighlightedTextSerializer
