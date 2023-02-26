from django.urls import path
from . import views


urlpatterns = [
	path('', views.index, name="list"),
	path('update_club/<str:pk>/', views.updateClub, name="update_club"),
	path('delete_club/<str:pk>/', views.deleteClub, name="delete_club"),
	path('table/', views.table_view, name="table"),
	path('delete_event/<int:pk>/', views.delete_event, name="delete_event"),
	path('update_event/<str:pk>/', views.update_event, name="update_event"),
]