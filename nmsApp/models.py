from django.db import models

# Create your models here.
class ServerInventory(models.Model):
    ip_address = models.CharField(max_length=100)
    os_type = models.CharField(max_length=50)
    server_type = models.CharField(max_length=50)
    
    def __str__(self):
        return self.ip_address
