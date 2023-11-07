from .models import Note
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Note.objects.all()
    # The serializer class for serializing output
    serializer_class = NoteSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]