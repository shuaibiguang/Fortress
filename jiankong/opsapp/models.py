from django.db import models

# Create your models here.
class serverlist(models.Model):
    ip = models.CharField(max_length=20)
    info = models.TextField()
    uptime = models.DateTimeField(auto_now = True)
    ctime = models.DateTimeField(auto_now_add = True)
