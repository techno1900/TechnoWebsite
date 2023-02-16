from django.db import models
import uuid
#Create your models here.


class project (models.Model):
    project_name = models.CharField(max_length=200)
    project_head = models.CharField(max_length=500)
    project_description = models.TextField(null = True, blank=True)
    project_image = models.ImageField(null =True, blank=True)
    project_link = models.CharField(max_length=5000, null =True, blank=True)
    project_youtube_link = models.CharField(max_length=5000, null=True,blank=True)
    project_catogery_name = models.ForeignKey('projectCatogery', on_delete=models.CASCADE, null=True, blank=True)
    project_created = models.DateTimeField(auto_now_add=True)
    project_id = models.UUIDField(default=uuid.uuid4, primary_key=True, unique=True, editable=False)

    def __str__(self):
        return str(self.project_name)

class projectCatogery(models.Model):

    project_catogery_name = models.CharField(max_length=500)
    project_category_created = models.DateTimeField(auto_now_add=True)
    project_category_id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True) 

    def __str__(self):
        return str(self.project_catogery_name)

