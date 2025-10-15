from django.db import models
from django.db.models import ForeignKey
from django.conf import settings


class UserFollows(models.Model):
    user = ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')

