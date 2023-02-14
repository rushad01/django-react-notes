from rest_framework import serializers
from core.models import Language, Catagory, Notes


class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'


class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
        fields = '__all__'


class NotesSerializer(serializers.ModelSerializer):
    language = serializers.StringRelatedField(many=False)
    catagory = serializers.StringRelatedField(many=False)

    class Meta:
        model = Notes
        fields = ['id', 'title', 'language',
                  'catagory', 'topic', 'note', 'updated_at']
