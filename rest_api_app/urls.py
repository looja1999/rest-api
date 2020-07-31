from django.conf.urls import url, include
from rest_framework import routers
from rest_api_app.views import StudentViewSets

router = routers.DefaultRouter()
router.register(r'student', StudentViewSets)

urlpatterns = [
    url(r'', include(router.urls)),
]
