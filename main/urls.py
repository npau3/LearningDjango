from django.urls import path
from . import views


urlpatterns = [
    path(r'', views.HomeListView.as_view(), name='home'),
    path(r'about', views.AboutListView.as_view(), name='about'),
    path(r'create', views.TaskCreateView.as_view(), name='create'),
    path(r'delete_page/<int:pk>', views.delete_page, name='delete_page'),
    path(r'update_page/<int:pk>', views.UpdateTaskView.as_view(), name='update_page'),
    path(r'search_page', views.SearchResultsView.as_view(), name='search_page'),
]