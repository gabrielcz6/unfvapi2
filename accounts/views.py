from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
import cv2
import tempfile
import numpy as np
from django.core.files.base import ContentFile
import requests
from PIL import Image,ExifTags
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from .utils import get_image_from_firebase, compare_images
from .models import CustomUser
import io
import base64

class UpdateCustomUser(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]  # Solo autenticación por token para esta vista
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user

class ImageView(APIView):
    authentication_classes = [TokenAuthentication]  # Solo autenticación por token para esta vista
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        #image_received = request.FILE.get('image')     
        image_received = request.POST.get('image')
        print(type(image_received))
        image_temp=base64.b64decode(image_received)
        image_temp=io.BytesIO(image_temp)
        image_temp = Image.open(image_temp)
        image_temp.save('temp_imagerequest.jpg')
        ## Descargar la imagen de Firebase
        image_url = request.user.urlfoto
        response = requests.get(image_url)
        #data = io.BytesIO(response.content)
        data=io.BytesIO(response.content)
        # Abrir los bytes como una imagen
        image2 = Image.open(data)
        try:
          for orientation in ExifTags.TAGS.keys():
              if ExifTags.TAGS[orientation] == 'Orientation':
                  break
          exif = dict(image2._getexif().items())

          if exif[orientation] == 3:
              image2 = image2.rotate(180, expand=True)
          elif exif[orientation] == 6:
              image2 = image2.rotate(270, expand=True)
          elif exif[orientation] == 8:
              image2 = image2.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
        # Las imágenes antiguas o las que no son de una cámara pueden no tener datos Exif
          pass
        puntaje=(compare_images(image_temp, image2))
        #print(puntaje)
        if puntaje>0.95:
                 status = "verificado con :"+ str(round(puntaje * 100, 1)) + "%"
                 return Response({'status': status})
        else:
                 status = 0
                 return Response({'status': status})



class CheckPhotoAPIView(generics.GenericAPIView):
    authentication_classes = [TokenAuthentication]  # Solo autenticación por token para esta vista
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get(self, request):
        user = request.user
        if user.tienefoto:
            return Response({"tienefoto": True}, status=status.HTTP_200_OK)
        else:
            return Response({"tienefoto": False}, status=status.HTTP_200_OK)
