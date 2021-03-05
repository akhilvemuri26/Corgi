from django.urls import path
from corgiapp import views

app_name = 'corgiapp'
urlpatterns = [
    path('secondpage/', views.secondpage, name='secondpage'),
]
