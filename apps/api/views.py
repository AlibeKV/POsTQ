from rest_framework.status import *

from rest_framework.viewsets import ModelViewSet

from .serializers import POstSerializer

from apps.app.models import POst

from rest_framework.permissions import IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

class POstSet(ModelViewSet):
    queryset = POst.objects.all()
    serializer_class = POstSerializer
    permission_classes = [IsAdminUser]
    authentication_classes = [JWTAuthentication]


