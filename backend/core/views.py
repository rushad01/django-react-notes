from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from core.models import Language, Catagory, Notes
from core.serializers import LanguageSerializer, CatagorySerializer, NotesSerializer

# Create your views here.


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'notes',
        'notes/<int:id>',
        'language',
        'catagory'
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
    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesSerializer(notes, many=True)
        return Response(serializer.data)
