from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Expense(models.Model):
    text   = models.CharField(max_length = 255)
    date   = models.DateTimeField()
    amount = models.DecimalField(max_digits= 10 ,decimal_places=2) 
    user   = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return "{}-{}".format(self.text,self.date)