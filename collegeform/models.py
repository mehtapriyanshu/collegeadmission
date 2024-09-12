from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 20)
    def __str__(self):
        return self.name


class Student(models.Model):

    departments = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    name = models.CharField(max_length = 20)
    fathername= models.CharField(max_length = 20)
    email = models.EmailField()
    Classs = models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)
    date_of_birth = models.DateField()
    updated = models.DateTimeField(auto_now = True)
    created = models.DateTimeField(auto_now_add= True)

    class Meta:
        ordering = ['-updated','-created']

    def __str__(self):
        return self.name




# class Fees(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees',null=True)  # Connect Fees to Student
#     total_fees = models.DecimalField(max_digits=10, decimal_places=2,null=True)  # Total fees amount
#     paid_fees = models.DecimalField(max_digits=10, decimal_places=2,null=True)   # Amount paid
#     due_fees = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)    # Remaining due
#     payment_date = models.DateField(null=True,blank=True)                                  # Date of payment

#     def __str__(self):
#         return f"Fees for {self.student}"