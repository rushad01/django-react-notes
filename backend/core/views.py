from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import generics
from core.models import Language, Catagory, Notes
from core.serializers import LanguageSerializer, CatagorySerializer, NotesSerializer
from django.http import Http404
from rest_framework import status

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'api/notes',
        'api/notes/<pk>',
        'api/languages',
        'api/catagories'
    ]

    return Response(routes)


class LanguageView(APIView):
    def get(self, request):
        language = Language.objects.all()
        serializer = LanguageSerializer(language, many=True)
        return Response(serializer.data)


class CatagoryView(APIView):
    def get(self, request):
        catagory = Catagory.objects.all()
        serializer = CatagorySerializer(catagory, many=True)
        return Response(serializer.data)


class NotesView(APIView):
    """
    List all notes, or create a new sNote.
    """

    def get(self, request, format=None):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class NotesDetail(APIView):
    """
    Retrieve , update or delete a single instance of Note from database
    """

    def get_object(self, pk):
        try:
            return Notes.objects.get(pk=pk)
        except Notes.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NotesSerializer(note)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        note = self.get_object(pk)
        serializer = NotesSerializer(note, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        note = self.get_object(pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
