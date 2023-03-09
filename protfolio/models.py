import uuid
from django.db import models

class Profile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    mail = models.EmailField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=14)
    upload = models.ImageField(upload_to='photos/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default="", null=False)

    class Meta:
        verbose_name_plural = "Profile"
        ordering = ['-created_at']
