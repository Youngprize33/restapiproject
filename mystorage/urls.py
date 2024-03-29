from django.urls import path, include
from .  import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('essay', views.PostViewSet)
router.register('Album', views.ImageViewSet)
router.register('Files', views.FileViewSet)

urlpatterns = [
    path('', include(router.urls))
]