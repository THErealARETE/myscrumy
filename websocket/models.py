from django.db import models

# Create your models here.

class Connection(models.Model):
    connection_id = models.CharField(max_length=255)

    def __str__(self):
        return self.id

class ChatMessage(models.Model):
    username = models.CharField(max_length=50)
    message = models.CharField(max_length=400)
    timestamp = models.CharField(max_length=100)