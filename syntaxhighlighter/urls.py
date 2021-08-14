from django.urls import path, include
from rest_framework.routers import DefaultRouter
from syntaxhighlighter import views

router = DefaultRouter()
router.register(r'snippets', views.SnippetsViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
]