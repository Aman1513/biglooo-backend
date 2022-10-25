from django.db import models
# Create your models here.

def PrivateImg(instance, imageName):
    return '/'.join(['PrivateJobs/images', str(instance.company_name), imageName])

class PrivateJobs(models.Model):
    company_name = models.CharField(max_length=20, null=False, blank=False)
    logo = models.ImageField(upload_to=PrivateImg, null=False, blank=False)
    job_title = models.CharField(max_length=50, null=False, blank=False)
    salary = models.CharField(max_length=15, null=False, blank=False)
    experience = models.CharField(max_length=50, null=False, blank=False)
    qualification = models.CharField(max_length=50, null=False, blank=False)
    location = models.CharField(max_length=50, null=False, blank=False)
    last_date = models.DateField()
    read_more = models.URLField(max_length=100, null=False, blank=False)
    apply = models.URLField(max_length=200, null=False, blank=False)
    search = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f'{self.company_name} {self.job_title}'

    

