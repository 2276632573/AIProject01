
 

from django.db import models

class BaseEntity(models.Model):
    id = None
    create_id = models.IntegerField(null=True, blank=True)
    update_id = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)
    remark = models.CharField(max_length=255, null=True, blank=True)
    version = models.PositiveIntegerField(default=0)

    class Meta:
        abstract = True

