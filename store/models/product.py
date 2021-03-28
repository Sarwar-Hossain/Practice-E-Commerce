from django.db import models
from .category import Category

# Create models here....

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=400, default="", null=True, blank=True)
    image = models.ImageField(upload_to="upload/products/")
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_products(request):
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_product_by_id(ids):
        return Product.objects.filter(id__in = ids)