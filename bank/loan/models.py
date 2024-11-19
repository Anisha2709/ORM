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