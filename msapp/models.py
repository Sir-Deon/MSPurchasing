from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    favorite = models.CharField(max_length=200, default="Normal")
    internal_ref = models.CharField(max_length=200)
    responsible = models.CharField(max_length=200)
    barcode = models.CharField(max_length=200)
    sales_price = models.IntegerField()
    cost = models.IntegerField()
    category = models.CharField(max_length=200)
    product_type = models.TextField(max_length=200)
    quantity_on_hand = models.IntegerField()
    forcated_quantity = models.IntegerField()
    activity = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=200)
    is_company = models.BooleanField(default=True)
    related_company = models.CharField(max_length=200)
    address_type = models.CharField(max_length=200)
    street = models.CharField(max_length=200)
    zip = models.IntegerField()
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    priority = models.CharField(max_length=200, default="Normal")
    order_reference = models.CharField(max_length=200)
    vendor = models.CharField(max_length=200)
    purchase_representative = models.CharField(max_length=200)
    order_deadline = models.CharField(max_length=200)
    activities = models.CharField(max_length=200)
    source_document = models.CharField(max_length=200, default="")
    Total = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.order_reference
