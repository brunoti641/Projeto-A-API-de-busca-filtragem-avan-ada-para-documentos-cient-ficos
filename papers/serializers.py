from rest_framework import serializers
from .models import Paper, Author
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id','name')
class PaperSerializer(serializers.ModelSerializer):
    authors = AuthorSerializer(many=True)
    class Meta:
        model = Paper
        fields = ('id','title','abstract','published_year','doi','authors','keywords','created_at')
