

from django.contrib.auth import views
from django.urls import path
from main import views as mviews


urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='registration/loggedout.html'), name='logout'),
    path('registration/', mviews.Registration.as_view(), name='registration')
]
