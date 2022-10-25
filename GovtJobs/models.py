from django.db import models
# Create your models here.

def GovtImg(instance, imageName):
    return '/'.join(['GovtJobs/images', str(instance.department_name), imageName])

class GovtJobs(models.Model):
    department_name = models.CharField(max_length=20, null=False, blank=False)
    logo = models.ImageField(upload_to=GovtImg, null=False, blank=False)
    job_title = models.CharField(max_length=50, null=False, blank=False)
    age_limit = models.CharField(max_length=30, null=False, blank=False)
    vacancy = models.CharField(max_length=20, null=False, blank=False)
    qualification = models.CharField(max_length=50, null=False, blank=False)
    last_date = models.DateField()
    read_more = models.URLField(max_length=100, null=False, blank=False)
    apply = models.URLField(max_length=200, null=False, blank=False)
    search = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return f'{self.department_name} {self.job_title}'
