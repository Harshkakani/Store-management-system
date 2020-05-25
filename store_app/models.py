from django.db import models

# Create your models here.


class Customer(models.Model):
    Customer_name = models.CharField(max_length=264, unique=True)
    Contact = models.IntegerField(unique=True)
    Address = models.TextField()
    Age = models.IntegerField()
    # Gender = models.

    def __str__(self):
        return self.Customer_name


class Stock(models.Model):
    Product_name = models.CharField(max_length=264, unique=True)
    Quantity = models.IntegerField()
    Expiry = models.DateField()
    Batch_number = models.IntegerField(unique=True)
    Rate = models.IntegerField()

    def __str__(self):
        return self.Product_name


class Sale(models.Model):
    Sale_number = models.IntegerField(unique=True)
    Customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product_name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    Batch_number = models.IntegerField(unique=True)
    Quantity = models.IntegerField()
    Expiry = models.DateField()
    Rate = models.IntegerField()
    Total_amount = models.IntegerField()
    Date = models.DateField()

    def __str__(self):
        return self.Sale_number


class Bill(models.Model):
    Customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Product_name = models.ForeignKey(Stock, on_delete=models.CASCADE)
    Batch_number = models.IntegerField()
    Amount = models.IntegerField()
    Sale_number = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return self


class SalesHistory(models.Model):
    Customer_name = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Date = models.DateField()
    Amount = models.IntegerField()
    Mode_of_Payment = models.CharField(max_length=10, unique=True)
    Sale_number = models.ForeignKey(Sale, on_delete=models.CASCADE)

    def __str__(self):
        return self


class Staff(models.Model):
    Staff_name = models.CharField(max_length=264, unique=True)
    Age = models.IntegerField()
    Salary = models.IntegerField()
    Contact = models.IntegerField()
    Hours_worked = models.IntegerField()
    Address = models.TextField()

    def __str__(self):
        return __str__(self.Staff_name)
