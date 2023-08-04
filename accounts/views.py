from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import CustomUserSerializer
from rest_framework.authentication import TokenAuthentication



class UpdateCustomUser(generics.UpdateAPIView):
    authentication_classes = [TokenAuthentication]  # Solo autenticación por token para esta vista
    permission_classes = [IsAuthenticated]
    serializer_class = CustomUserSerializer

    def get_object(self):
        return self.request.user