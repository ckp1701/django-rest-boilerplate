from django.db import models
from django.utils import timezone


class TimeStampedModel(models.Model):
    """
     Base class for adding created_at and updated_at fields to all other models.
    """
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.updated_at = timezone.now()
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)
