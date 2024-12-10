from rest_framework import generics
from .models import Ping
from .serializers import PingSerializer
from rest_framework import permissions


class PingListCreateAPIView(
    generics.ListCreateAPIView
):
    queryset = Ping.objects.all()
    serializer_class = PingSerializer
    permission_classes=[permissions.AllowAny]
    # lookup_field = 'pk' 
    # authentication_classes= [TokenAuthentication]
    # # permission_classes = [permissions.IsAdminUser,
    # #     IsStaffEditorPermission]
    
    
    def perform_create(self, serializer):
        return super().perform_create(serializer)