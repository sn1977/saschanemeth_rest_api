from django.db import models
import datetime
# from django.conf import settings


class Todo(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    # created_at = models.DateField(auto_now_add=True)
    created_at = models.DateField(default=datetime.date.today)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
