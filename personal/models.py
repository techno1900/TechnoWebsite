from django.db import models
import uuid
# Create your models here.

class personalDetails(models.Model):
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=12)
    email = models.CharField(max_length=500)
    profile_image = models.ImageField(null=True, blank=True)
    bio = models.TextField()
    profile_created = models.DateTimeField(auto_now_add=True)
    user_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)

    def __str__(self):
        return str(self.name)
        
