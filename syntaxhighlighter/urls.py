from django.urls import path
from .views import SnippetList, GetSnippet
urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='list-snippets'),
    path('snippets/<int:pk>/', GetSnippet.as_view(), name='get-snippets'),
]