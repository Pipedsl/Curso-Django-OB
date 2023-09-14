from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
