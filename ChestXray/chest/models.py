from django.db import models
from django.contrib.auth.models import User
# Create your models here.

    
class Diagnosis(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to="Predictions")
    results = models.CharField(max_length=50)
    def __str__(self):
        return self.results
