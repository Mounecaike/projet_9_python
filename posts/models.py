from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import ForeignKey, ImageField
from django.db.models.fields import TextField, DateTimeField, PositiveSmallIntegerField


class Ticket(models.Model):
    title = models.CharField(max_length=128, default="")
    description = TextField(max_length=2048, blank=True)
    user = ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = ImageField(null=True, blank=True)
    time_created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"


class Review(models.Model):
    ticket = ForeignKey(to=Ticket, on_delete=models.CASCADE)
    rating = PositiveSmallIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user = ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    headline = models.CharField(max_length=128, default="")
    body = TextField(max_length=8192, blank=True)
    time_created = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ticket}"