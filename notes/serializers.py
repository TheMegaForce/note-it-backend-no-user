from .models import Note
from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Our NoteSerializer
class NoteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        # The model it will serialize
        model = Note
        # the fields that should be included in the serialized output
        fields = ['id', 'title', 'content']