from django.urls import path

from . import views

app_name = 'racer'
urlpatterns = [
    path('',views.index, name='index'),
    path('<str:district_num>/', views.racer, name='racer')
  #  path('add_racer/', views.add_racer, name='add_racer')
]