from django.db import models

# Create your models here.
class Chemist(models.Model):
    id = models.AutoField(primary_key = True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_no = models.CharField(max_length=255)
    chemist_email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

#create a model for the medicine
class Medicine(models.Model):
    medicine_id = models.AutoField(primary_key = True)
    medicine_name = models.CharField(max_length=255)
    medicine_type = models.CharField(max_length=255)
    buy_price = models.CharField(max_length=25)
    sell_price = models.CharField(max_length=25)
    exp_date = models.DateField()
    id = models.ForeignKey(Chemist , on_delete= models.CASCADE)
    description = models.CharField(max_length=255)
    instock_qty = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
#create a model medical details
class MedicalDetails(models.Model):
    medical_details_id = models.AutoField(primary_key = True)
    medicine_id = models.ForeignKey(Medicine,on_delete= models.CASCADE)
    salt_name = models.CharField(max_length=255)
    salt_qty = models.CharField(max_length=25)
    salt_type = models.CharField(max_length=25)
    added_on = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)
    objects = models.Manager()
# create a model for the staff members
class Staff(models.Model):
    staff_id = models.AutoField(primary_key = True)
    fname = models.CharField(max_length= 25)
    sname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone_no= models.CharField(max_length=25)
    address = models.CharField(max_length=255)
    added_on  = models.DateTimeField(auto_now_add=True)
    objects = models.Manager()

#create a model of customers
class Customer(models.Model):
    customer_id = models.AutoField(primary_key = True)
    fname = models.CharField(max_length=25)
    sname = models.CharField(max_length=25)
    lname = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=15)
    added_on = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()
# create model on billing
class Bill(models.Model):
    bill_id = models.AutoField(primary_key = True)
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    bill_date = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()

#create  a model on billing details
class BillDetails(models.Model):
    bill_details_id = models.AutoField(primary_key = True)
    bill_id = models.ForeignKey(Bill , on_delete= models.CASCADE)
    medicine_id = models.ForeignKey(Medicine, on_delete= models.CASCADE)
    quantity = models.IntegerField()
    added_on = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()

#create a model on customer requests
class CustomerRequest(models.Model):
    requets_id = models.AutoField(primary_key = True)
    customer_name = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=25)
    medicine_details = models.CharField(max_length=255)
    status = models.BooleanField(default=False)
    added_on = models.DateTimeField(auto_now_add= True)
    objects = models.Manager()




