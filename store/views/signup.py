from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self, request):
        return render(request, 'signup.html')        
    def post(self, request):
        postData = request.POST
        first_name = postData.get('first_name')
        last_name = postData.get('last_name')
        phone = postData.get('phone')
        email = postData.get('email')
        password = postData.get('password') 
        # saving values in form fields
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email':email
        }
        # validation
        error_message = None
        
        customer = Customer(first_name = first_name, last_name = last_name, phone = phone, email = email, password= password)
        error_message = self.validateCustomer(customer)
        # saving data
        if not error_message:
            # hashing password
            customer.password = make_password(customer.password)
            customer.save()
            #customer.register()
            
            return redirect('store:home')
        else: 
            data= {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)
        
    def validateCustomer(self, customer):
        error_message = None
        if not customer.first_name:
            error_message = "Frist Name Required !!"
        elif len(customer.first_name) < 3:
            error_message = "First name must be 3 character long or more"
        elif not customer.last_name: 
            error_message = "Last Name Required !!"
        elif len(customer.last_name) < 3:
            error_message = "Last name must be 3 character long or more"
        elif not customer.phone:
            error_message = "Phone Number is required"
        elif len(customer.phone) < 10: 
            error_message =  "Phone Number must 10 character long"
        elif not customer.password:
            error_message = "Password is required"
        elif len(customer.password) < 6: 
            error_message  = "Password must 6 character long"
        elif customer.isExist():
            error_message = "Email Address Already Registered"
        
        return error_message