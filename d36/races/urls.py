from django.urls import path

from . import views

app_name = 'races'
urlpatterns = [
    path('',views.index, name='index'),
    path('<str:event_name>/', views.event, name='event'),
    path('<int:year>/<str:race>/', views.race)
]