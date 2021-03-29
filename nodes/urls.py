from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import NodeViewSet

router = DefaultRouter()
router.register(r'/nodes', viewset=NodeViewSet)

urlpatterns = []
urlpatterns += router.urls
