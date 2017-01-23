from django.db import models

# Create your models here.
class wx_user(models.Model):
    token = models.TextField()
    user_name = models.CharField(max_length=20)
    ctime = models.DateTimeField(auto_now_add = True)
