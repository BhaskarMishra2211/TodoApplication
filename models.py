from django.db import models
from django.utils import timezone
import datetime
import schedule
import time
from django.conf import settings
#from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
    task = models.TextField()
    name = models.CharField(max_length = 20,default = "")
    completed = models.BooleanField(default = False)
    created_date = models.DateTimeField(default = timezone.now)
    deadline = models.DateTimeField(null=False, default= timezone.now)

    
    def get_time_diff(self):
        timediff = timezone.now() - self.deadline
        if timediff == 0:
            return 0
        else:
            return abs(int(timediff.total_seconds()*1//60*1//60))

    schedule.every().hour.do(get_time_diff) 


User_Choices = (
    ("bhaskar","bhaskar"),
    ("avanisharma","avanisharma"),
)
class Assign_task(models.Model):
    task_name = models.CharField(max_length=50)
    assigned_date = models.DateTimeField(default = timezone.now)
    deadline = models.DateTimeField(null = False,default = timezone.now)
    Assigned_to = models.CharField(choices = User_Choices,max_length = 100,default = '1')


class AssignedTask(models.Model):
    Task_Name = models.CharField(max_length = 100)
    SELECT_USER = models.CharField(max_length = 100)
    start_date = models.DateField()
    end_date = models.DateField()


