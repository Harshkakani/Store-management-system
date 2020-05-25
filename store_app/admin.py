from django.contrib import admin
from store_app.models import Bill, Customer, Sale, SalesHistory, Staff, Stock
# Register your models here.
admin.site.register(Bill)
admin.site.register(Customer)
admin.site.register(Sale)
admin.site.register(SalesHistory)
admin.site.register(Staff)
admin.site.register(Stock)
