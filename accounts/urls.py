from django.urls import path
from .views import UpdateCustomUser

urlpatterns = [
    path('update/', UpdateCustomUser.as_view(), name='update'),
]

