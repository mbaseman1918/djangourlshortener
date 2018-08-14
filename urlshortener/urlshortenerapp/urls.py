from django.urls import path
from . import views

app_name = 'urlshortenerapp' # for namespacing
urlpatterns = [
    path('', views.index, name='index'),
    path('redirect/<url_short>/', views.redirect, name='redirect'),
    path('redirect_typed/', views.redirect_typed, name='redirect_typed'),
]
