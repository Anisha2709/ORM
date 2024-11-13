![image](https://github.com/user-attachments/assets/9062bf08-fb43-4407-9c66-f89acc7086b5)# Ex02 Django ORM Web Application
## Date: 13.11.2024 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![ER DIAGRAM ORM EX 02](https://github.com/user-attachments/assets/a0624110-0285-4086-b130-72e699f0e282)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
models.py : 

from django.db import models
from django.contrib import admin
class Bank (models.Model):
    loan_id=models.IntegerField(primary_key=True)
    cust_acno=models.IntegerField()
    cust_name=models.CharField(max_length=100)
    loan_amt=models.FloatField()
    loan_type=models.CharField(max_length=100)
 
class BankAdmin(admin.ModelAdmin):
    list_display=('loan_id','loan_type','loan_amt','cust_acno')

admin.py :

from django.contrib import admin
from .models import Bank,BankAdmin
admin.site.register(Bank,BankAdmin)

## OUTPUT

![image](https://github.com/user-attachments/assets/06492f97-6f01-42ca-a90f-5f8bd1668e1d)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
