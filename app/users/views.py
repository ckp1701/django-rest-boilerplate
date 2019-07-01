from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from app.users.models import UserConfiguration
from app.users.serializers import UserConfigurationSerializer


@authentication_classes((BasicAuthentication, TokenAuthentication))
@permission_classes((IsAuthenticated,))
class UserConfigurationViewSet(ModelViewSet):
    serializer_class = UserConfigurationSerializer

    def get_queryset(self):
        user = self.request.user
        return UserConfiguration.objects.filter(user=user)
