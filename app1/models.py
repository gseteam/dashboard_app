from django.db import models


class People_model(models.Model):
    Id=models.AutoField(primary_key="True")
    name=models.CharField(max_length=30)
    vacation_plan=models.CharField(max_length=100,default='none')
    visa_status=models.CharField(max_length=100,default='none')
    def __unicode__(self):
        return self.name

class Activity_model(models.Model):
    Activity_Id=models.AutoField(primary_key="True") #auto field addeded
    Activity_Name=models.CharField(max_length=20)
    Activity_type=models.CharField(max_length=20)
    state=models.CharField(  max_length=10,default='1')
    Customer_name=models.CharField(max_length=20,default='APJ')
    Description=models.CharField(max_length=200,default='none')
    def __unicode__(self):
        return self.Activity_Name

class detail_model(models.Model):
    Act_name=models.CharField(max_length=20)
    emp_name=models.CharField(max_length=20)
    def __unicode__(self):
      return self.Act_name

class settings_model(models.Model):
    Id=models.AutoField(primary_key="True")
    Project_Allocated=models.CharField(max_length=10,default=4)



