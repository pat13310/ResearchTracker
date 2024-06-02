from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from serializers.TextSerializer import TextSerializer
from .utils import TextProcessor


class SimplifyTextView(APIView):
    def post(self, request, format=None):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            processor = TextProcessor()
            simplified_text = processor.simplify_text(text)
            capitalized_text = processor.capitalize_sentences(simplified_text)
            return Response({'simplified_text': capitalized_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SummarizeTextView(APIView):
    def post(self, request, format=None):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            processor = TextProcessor()
            summarized_text = processor.summarize_text(text)
            return Response({'summarized_text': summarized_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TranslateTextView(APIView):
    def post(self, request, format=None):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            processor = TextProcessor()
            translated_text = processor.translate_text(text)
            return Response({'translated_text': translated_text}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
