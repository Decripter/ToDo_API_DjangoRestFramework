from rest_framework import urlpatterns
from rest_framework import routers
from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls
