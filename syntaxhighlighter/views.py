from django.contrib.auth.models import User


from rest_framework import viewsets
from rest_framework import permissions, renderers
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.decorators import api_view, action, renderer_classes

from .serializers import HighlightedTextSerializer, UserSerializer
from .models import Snippets
from .permissions import IsOwnerOrReadOnly

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This model automatically provides `list` and `retrieve` actions 
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SnippetsViewSet(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    queryset = Snippets.objects.all()
    serializer_class =HighlightedTextSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]     
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlights(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)



    
