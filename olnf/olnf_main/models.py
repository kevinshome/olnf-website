from django.db import models

class Member(models.Model):
    name = models.TextField()
    description = models.TextField()
    bg_image_name = models.TextField()
    social_media = models.JSONField()
