from django.urls import path
from recipes.views import home, sobre, contacto


urlpatterns = [
    path('', home),
    path('sobre/', sobre),
    path('contacto/', contacto),
]
