from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from api.serializers import UserViewSet, TeamViewSet, TaskViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'teams', TeamViewSet)
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
