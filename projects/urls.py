from django.urls import path
from projects import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register("", views.ProjectInfo_ViewSet)

urlpatterns = router.urls
