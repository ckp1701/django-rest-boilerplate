from django.urls import include, path
from rest_auth.registration.views import VerifyEmailView
from app.users.views import UserConfigurationViewSet
from rest_framework import routers

# app_name = 'v1'
router = routers.SimpleRouter()

router.register(r'configurations', UserConfigurationViewSet, base_name='configurations')

urlpatterns = [
    # auth endpoints
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),

]

urlpatterns += router.urls
