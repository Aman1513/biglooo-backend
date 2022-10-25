from django.db import models
# Create your models here.

class LoginDetail(models.Model):
    name = models.CharField(max_length=80, null=False, blank=False)
    imageUrl = models.URLField(max_length=500, null=False, blank=False)
    givenName = models.CharField(max_length=50, null=False, blank=False)
    familyName = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=80, null=False, blank=False, unique=True)
    googleId = models.CharField(max_length=40, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
