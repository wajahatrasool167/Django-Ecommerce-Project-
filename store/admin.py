from django.contrib import admin
from .models.category import Category
from .models.product import Product
from .models.customer import Customer
from .models.orders import Order


# Register your models here.
admin.site.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
    
    
admin.site.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['category','name','price']
    
    
admin.site.register(Customer)
class AdminCustomer(admin.ModelAdmin):
    list_display = ['first_name']
    
admin.site.register(Order)
class AdminOrder(admin.ModelAdmin):
    list_display = ['customer']
    
    

