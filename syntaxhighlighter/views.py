from django.shortcuts import render
from rest_framework import permissions, renderers
from rest_framework.generics import *
from rest_framework.response import Response
from .serializers import HighlightedTextSerializer
from .models import Snippets
from .permissions import IsOwnerOrReadOnly


class SnippetList(ListAPIView):
    queryset = Snippets.objects.all()
    serializer_class = HighlightedTextSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, 
        IsOwnerOrReadOnly
    ]

class SnippetCreateRetrieve(CreateAPIView, RetrieveAPIView, GenericAPIView):

    queryset = Snippets.objects.all()
    serializer_class = HighlightedTextSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class SnippetHighlight(GenericAPIView):
    queryset = Snippets.objects.all()
    renderers_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)
    