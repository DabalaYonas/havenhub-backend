from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('utilities', views.UtilityView, 'Utilities')
router.register('types', views.TypeView, 'types')
router.register('images', views.ImageView, 'images')

urlpatterns = [
    path('api/', include(router.urls)),
    path('<str:id>/', include(router.urls)),
]
