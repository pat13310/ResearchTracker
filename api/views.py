from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from publications.models import Publication
from serializers.PublicationSerializer import PublicationSerializer
import uuid


class CreateDOIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        data['doi'] = self.generate_doi()
        serializer = PublicationSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def generate_doi(self):
        return f"10.1234/{uuid.uuid4()}"


class PublicationDetailView(generics.RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    lookup_field = 'doi'
