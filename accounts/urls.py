
from django.contrib.auth import views as auth_views
from django.urls import path
from main import views


urlpatterns = [
    path('', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/loggedout.html'), name='logout'),
    path('registration/', views.Registration.as_view(), name='registration')
]
