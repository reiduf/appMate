from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

# Create your models here.

class Job(models.Model):
    company = models.CharField(max_length=50)
    date = models.DateField('Applied Date')
    salary = models.IntegerField()
    position = models.CharField(max_length=50)
    notes = models.TextField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    connection = models.OneToOneField(Connection, primary_key=True)
    
    def __str__(self):
        return f'{self.company} ({self.id})'
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'job_id': self.id})


class Todo(models.Model):
    description = models.TextField(max_length=200)
    done = models.BooleanField(default=False)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'
    

class Status(models.Model):
    description = models.TextField(max_length=200)
    date = models.DateField('Status Date')
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.description} ({self.id})'




