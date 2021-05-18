from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Friend(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    age = models.IntegerField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name