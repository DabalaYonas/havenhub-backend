
from django.urls import path, include
from . import views
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('register', views.RegisterView, 'register')
# # router.register('login', views.LoginView, 'login')

urlpatterns = [
    path('api/register/', views.RegisterView.as_view()),
    path('api/login/', views.LoginView.as_view()),
    path('api/', views.UserView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),
]
