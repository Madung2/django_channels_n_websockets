from django.db import models

# Create your models here.
class ChatModel(models.Model):
    comment = models.CharField("텍스트", max_length=300, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
