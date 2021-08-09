from django.urls import path
from .views import SnippetList, SnippetCreateRetrieve, SnippetHighlight
urlpatterns = [
    path('snippets/', SnippetList.as_view(), name='list-snippets'),
    path('snippets/retrieve/<int:pk>/', SnippetCreateRetrieve.as_view(), name='get-snippets'),
    path('snippets/create/', SnippetCreateRetrieve.as_view(), name='create-snippets'),
    path('snippets/highlight/', SnippetHighlight.as_view(), name='get-snippets-highlight')
]