from pyexpat import model
from statistics import mode
from django.db import models
import random

# Create your models here.



class User(models.Model):
    userName = models.CharField(max_length=255,null=False,blank=False)
    twitterHandle= models.CharField(max_length=255,null=True,blank=False)
    walletAddress = models.CharField(max_length=255,null=False,blank=False)
    whoReferedMe = models.CharField(max_length=255,null=True,blank=True)
    myRefrealCode = models.CharField(max_length=255,null=True,blank=True)
    isKycVerified = models.CharField(max_length=255,null=True,blank=True,default="False")
    

    def __str__(self):
        return self.walletAddress
 
class KYCData(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    FullName = models.CharField(max_length=255,null=False,blank=False)
    IdNumber= models.CharField(max_length=255,null=False,blank=False)
    documentFile = models.FileField(upload_to = 'Files/')
    image = models.ImageField(upload_to='images/',blank=True)

    def __str__(self):
        return self.IdNumber

class NoOfWeeks(models.Model):
    quizzId = models.CharField(max_length=255,null=False,blank=False)

    def __str__(self):
        return self.quizzId

class Question(models.Model):
    weekId = models.ForeignKey(NoOfWeeks,on_delete=models.CASCADE)
    question = models.CharField(max_length=255,null=False,blank=False)
    op1 = models.CharField(max_length=200,null=True)
    op2 = models.CharField(max_length=200,null=True)
    op3 = models.CharField(max_length=200,null=True)
    op4 = models.CharField(max_length=200,null=True)
    ans = models.CharField(max_length=200,null=True)
    
    def __str__(self):
        return str(self.id)

class courseCompleted(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    isWeek1Completed = models.BooleanField(default=False)
    isWeek2Completed = models.BooleanField(default=False)
    isWeek3Completed = models.BooleanField(default=False)
    isWeek4Completed = models.BooleanField(default=False)
    score1 = models.CharField(max_length=200,null=True,blank=True)
    score2 = models.CharField(max_length=200,null=True,blank=True)
    score3 = models.CharField(max_length=200,null=True,blank=True)
    score4 = models.CharField(max_length=200,null=True,blank=True)


    def __str__(self):
        return "course"
