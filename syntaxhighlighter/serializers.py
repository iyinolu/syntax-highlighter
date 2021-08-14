from django.contrib.auth.models import User
from pygments import highlight
from rest_framework import serializers
from .models import Snippets

class HighlightedTextSerializer(serializers.HyperlinkedModelSerializer):
    # NOTE: "source" points to the Snippet model "owner" then => "username" field
    # Hence, serializer.save() adds request.user to the model user field
    user = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name="snippets-highlights", format='html')
    class Meta: 
        model = Snippets
        fields = [
            'url', 'id', 'highlight', 'title',
            'code', 'created', 'user', 'code', 
            'linenos', 'language', 'style'
        ]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, queryset=Snippets.objects.all(), view_name='snippets-detail')
    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'snippets']