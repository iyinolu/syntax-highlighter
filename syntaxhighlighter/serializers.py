from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Snippets

class HighlightedTextSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='owner.username')
    class Meta: 
        model = Snippets
        fields = ['title', 'code', 'created', 'user']
