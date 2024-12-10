from os import path
from rest_framework.routers import DefaultRouter

from .views import PingListCreateAPIView


from .viewsets import PingViewSet

router = DefaultRouter()
router.register(r'', PingViewSet, basename='ping')

urlpatterns = [
    # path('creer/', PingListCreateAPIView.as_view()),
] + router.urls