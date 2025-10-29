from django.db import models
from django.db.models import ForeignKey
from django.conf import settings


class UserFollows(models.Model):
    user = ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')
    followed_user = ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followed_by')


class UserBlock(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blocking"
    )
    blocked_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="blocked_by"
    )

    class Meta:
        unique_together = ('user', 'blocked_user')

    def __str__(self):
        return f"{self.user.username} a bloqué {self.blocked_user.username}"
