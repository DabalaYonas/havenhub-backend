
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('', views.UserView, 'user')

urlpatterns = [
    path('api/', include(router.urls)),
]
