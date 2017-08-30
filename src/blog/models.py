from django.db import models


# Create your models here.

class Articals(models.Model):
    articalID = models.AutoField(primary_key=True)
    SUBJECTS = (
        ('ML', 'Machine Learning'),
        ('DB', 'Database'),
        ('FED', 'Front-End Development')
    )
    title = models.CharField(max_length=120)
    subject = models.CharField(max_length=30, choices=SUBJECTS)
    txt_content = models.CharField(max_length=120, null=True, blank=True)
    images = models.CharField(max_length=120, null=True, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
