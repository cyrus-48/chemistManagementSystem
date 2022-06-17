from django.contrib import admin

# Register your models here.
from chemistApp.models import Chemist, Medicine, Staff, Bill, CustomerRequest, BillDetails, Customer, MedicalDetails

admin.site.register(Chemist)
admin.site.register(Medicine)
admin.site.register(Staff)
admin.site.register(Bill)
admin.site.register(CustomerRequest)
admin.site.register(BillDetails)
admin.site.register(Customer)
admin.site.register(MedicalDetails)
