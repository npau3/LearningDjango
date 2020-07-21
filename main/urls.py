from django.urls import path, include
from . import views


urlpatterns = [
    path('about', views.about, name='about'),
    path('create', views.create, name='create'),
    path('update_page', views.update_page, name='update_page')
]