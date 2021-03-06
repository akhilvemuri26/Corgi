from django.urls import path
from corgiapp import views

app_name = 'corgiapp'
urlpatterns = [
    path('secondpage/', views.secondpage, name='secondpage'),
    path('register/', views.register, name ='register'),
    path('user_login/', views.user_login, name='user_login'),
    ]
