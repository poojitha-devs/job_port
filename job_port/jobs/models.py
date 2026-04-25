from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Job(models.Model):
    recruiter = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=1000)
    description = models.TextField()
    salary = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='logos/', null=True, blank=True)
    company = models.CharField(max_length=100)
    posted_on = models.DateField(auto_now_add=True,null=True,blank=True)

class Application(models.Model):
    applicant=models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='applications_as_applicant')
    job=models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    resume=models.FileField(upload_to='resume/')
    
    def __str__(self):
        return f"{self.applicant.username} - {self.job.title}"

                                   