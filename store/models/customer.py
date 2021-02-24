from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    password = models.CharField(max_length=500)
    repassword = models.CharField(max_length=500, default='')

          
    def is_exits(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            False
    
    @staticmethod  
    def get_user_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            False
