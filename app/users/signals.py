from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from app.users.models import UserConfiguration


@receiver(post_save, sender=get_user_model())
def user_post_save(sender, instance, created, *args, **kwargs):
    if created:
        has_configuration = UserConfiguration.objects.filter(user=instance).exists()
        if not has_configuration:
            UserConfiguration.objects.create(user=instance)
