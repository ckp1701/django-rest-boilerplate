from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext as _

from app.core.models import TimeStampedModel


class CustomUser(AbstractUser):
    def __str__(self):
        return self.email


class UserConfiguration(TimeStampedModel):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return _(f"User: {self.user}")
