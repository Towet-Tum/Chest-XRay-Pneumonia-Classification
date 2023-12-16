from django.urls import path 
from . import views 

urlpatterns = [
    path('index/<int:id>/', views.index, name='index'),
    path('register/', views.register, name="register"),
    path('user_login/', views.user_login, name="user_login"),
    path('login_success/', views.login_success, name="login_success")

]