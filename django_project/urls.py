from drf_spectacular.views import (
SpectacularAPIView,
SpectacularRedocView,
SpectacularSwaggerView, # new
)
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("posts.urls")), 
    path("api/v2/", include('accounts.urls')),  
    path("api-auth/", include("rest_framework.urls")), # new
    path("api/v1/dj-rest-auth/", include("dj_rest_auth.urls")), # new
    path("api/v1/dj-rest-auth/registration/", # new
         include("dj_rest_auth.registration.urls")), #para registrar nuevo usuario
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"), # new
    path("api/schema/redoc/", SpectacularRedocView.as_view(
            url_name="schema"), name="redoc",), # new  
    path("api/schema/swagger-ui/", SpectacularSwaggerView.as_view(
       url_name="schema"), name="swagger-ui"), # new  
                
]
