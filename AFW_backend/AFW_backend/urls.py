# albertafirewatch_backend/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from fires.views import WildfireViewSet

router = DefaultRouter()
router.register(r'fire-reports', WildfireViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
