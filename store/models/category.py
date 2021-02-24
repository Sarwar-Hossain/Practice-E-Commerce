from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)
    
    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    @staticmethod
    def get_all_categories(request):
        return Category.objects.all()
  
    def __str__(self):
        return self.name
