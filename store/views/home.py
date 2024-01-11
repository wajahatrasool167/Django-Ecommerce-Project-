from django.shortcuts import redirect, render
from store.models.product import Product
from store.models.category import Category
from django.views import View


# Create your views here.   
class Index(View):
    def post(self, request):
        #getting product id
        product = request.POST.get('product', None)
        remove = request.POST.get('remove')
        # Getting the existing cart from the session       
        cart = request.session.get('cart',{})  
        if cart:
            # Updating the quantity of the product in the cart
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                         cart[product] = quantity-1   
                else:
                    cart[product] = quantity+1
            else:
                cart[product] = 1        
        else:
            cart = {}
            cart[product] = 1           
            
        request.session['cart'] = cart
        print('cart', request.session['cart'])
        return redirect('store:home')      
     
    # def post(self, request):
    #     # Getting product id from the POST request
    #     product = request.POST.get('product',{}) 
    #     # Getting the existing cart from the session
    #     cart = request.session.get('cart', {})
    #     # Updating the quantity of the product in the cart
    #     quantity = cart.get(product, 0)
    #     cart[product] = quantity + 1
    #     # Saving the updated cart back to the session
    #     request.session['cart'] = cart

    #     print('cart', request.session['cart'])

    #     # Redirecting to the home view
    #     return redirect('store:home')
    
    def get(self, request):
        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        products = None
        categories = Category.get_all_categories()
        categoryID = request.GET.get('category')
        if categoryID:
            products = Product.get_all_products_by_categoryid(categoryID)
        else:
            products = Product.get_all_products()    
        data = {}
        data['products'] = products
        data['categories'] = categories
        
        print("you are: " ,request.session.get('email'))
    
    
        return render(request, 'index.html', data)



        

        
        