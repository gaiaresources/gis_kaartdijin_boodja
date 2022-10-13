"""Kaartdijin Boodja Users Django Application URLs."""


# Third-Party
from rest_framework import routers

# Local
from . import views


# Router
router = routers.DefaultRouter()
router.register("users", views.UserViewSet)
router.register("groups", views.GroupViewSet)


# Users URL Patterns
urlpatterns = router.urls
