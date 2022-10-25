from django.db import models
# Create your models here.

def BlogImg(instance, imageName):
    return '/'.join(['Blog/images', str(instance.department_name), imageName])

class Blog(models.Model):
    heading = models.CharField(max_length=200, null=False, blank=False)
    img = models.ImageField(upload_to=BlogImg, null=False, blank=False)
    blog = models.TextField(null=False, blank=False)

    def __str__(self):
        return f'{self.heading}'
