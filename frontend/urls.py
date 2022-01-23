from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('upload/', views.upload, name='upload'),
    path('list_data/', views.list_data, name='list_data'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/', views.delete, name='delete')
]
