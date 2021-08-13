from django.db import models

# Create your models here.

class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100, default="")
    product_price = models.IntegerField(default=0)
    category = models.CharField(max_length=100, default="")
    subcategory = models.CharField(max_length=100, default="")
    desc = models.CharField(max_length=500, default="")
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/Images", default="")


    def __str__(self):
        return self.product_name
