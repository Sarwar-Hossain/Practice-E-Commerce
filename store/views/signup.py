from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View


class Signup(View):
    def get(self, request):
        return render(request, "signup.html")

    def post(self, request):
        postData = request.POST
        first_name = postData.get('firstname')
        last_name = postData.get('lastname')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password')
        repassword = postData.get('repassword')

        # customer object
        customer = Customer(first_name=first_name,
                            last_name=last_name,
                            phone=phone,
                            email=email,
                            password=password,
                            repassword=repassword)

        # Validation
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }

        error_message = self.validate_customer(customer)

        if not error_message:
            customer.password = make_password(customer.password)
            customer.repassword = make_password(customer.repassword)
            customer.save()
            return redirect("homepage")
        else:
            data = {
                "error": error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

        # Validation for Sign up Page
        
    def validate_customer(self, customer):

        error_message = None

        if not customer.first_name:
            error_message = "First Name is Required"
        elif len(customer.first_name) < 4:
            error_message = "First Name should be more than 4 Characters!!"
        elif not customer.last_name:
            error_message = "Last Name Required"
        elif len(customer.last_name) < 4:
            error_message = "Last Name should be more than 4 Characters!!"
        elif not customer.phone:
            error_message = "Phone Number Required"
        elif len(customer.phone) < 11:
            error_message = "Phone Number Less than 11"
        elif not customer.email:
            error_message = "Email Required"
        elif not customer.password:
            error_message = "Enter Password"
        elif len(customer.password) < 6:
            error_message = "Password Less than 6"
        elif not customer.repassword:
            error_message = "Re-Enter Your Password"
        elif not customer.password == customer.repassword:
            error_message = "Password does not Match!!"
        elif customer.is_exits():
            error_message = "Email Address Already Exits"
        return error_message
