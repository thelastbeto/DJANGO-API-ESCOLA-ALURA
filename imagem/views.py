from rest_framework import viewsets
from imagem.serializer import ImagemSerializer
from imagem.models import Imagem

class ImagemViewSet(viewsets.ModelViewSet):
    queryset = Imagem.objects.all()
    serializer_class = ImagemSerializer