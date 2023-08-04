from django.urls import path
from .views import UpdateCustomUser,ImageView

urlpatterns = [
    path('update/', UpdateCustomUser.as_view(), name='update'),
    path('uploadimage/', ImageView.as_view(), name='file_upload'),
]

