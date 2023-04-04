from rest_framework import serializers
from imagem.models import Imagem

class ImagemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imagem
        fields = '__all__'