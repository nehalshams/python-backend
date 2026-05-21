from django.db import models
import uuid

class BaseModel(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4, 
        unique= True,
        primary_key=True,
        editable=False
        )
    
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    class Meta:
        abstract = True

class Transaction(BaseModel):
    amount = models.FloatField()
    description = models.CharField(max_length=255)

