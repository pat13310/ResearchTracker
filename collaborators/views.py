from rest_framework import viewsets
from .models import Collaborator
from serializers import CollaboratorSerializer


class CollaboratorViewSet(viewsets.ModelViewSet):
    queryset = Collaborator.objects.all()
    serializer_class = CollaboratorSerializer
