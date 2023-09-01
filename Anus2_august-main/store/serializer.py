from rest_framework import serializers
from .models import Chapter, Book

class ChapterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chapter
        fields = ['title', 'content']


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['name', 'genre']