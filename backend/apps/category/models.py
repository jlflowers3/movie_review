from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Category(models.Model):
    class Meta(object):
        db_table = 'category'

    name = models.CharField(
        'name', blank=False, null=False, max_length=50, db_index=True, default='Anonymous'
    )

    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
    
    def __str__(self):
        return self.name