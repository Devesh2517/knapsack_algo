from django.urls import path
from .views import *
# from drf_spectacular.views import SpectacularAPIView,SpectacularSwaggerView



urlpatterns = [
path('item',ItemView.as_view(),name='item'),
]
