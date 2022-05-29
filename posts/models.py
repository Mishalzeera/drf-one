from django.db import models

# Create your models here.

class Post(models.Model):
      """Post model for my amazing blog"""
      title = models.CharField(max_length=255)
      body = models.CharField(max_length=2000)

      def __str__(self):
            return self.title
