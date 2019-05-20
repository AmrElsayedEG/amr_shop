from django.http import HttpResponse
from django.shortcuts import render
from cart.forms import CartAddProductForm
# Create your views here.
from mainsite.models import addProduct
from orders.models import OrderItem


def home(request):
    r = request.user
    x = OrderItem.objects.all()
    f_arr = []
    s_arr = []
    prod_ids = []
    final_list = []
    for i in x:
        f_arr.append(i)

    for i in f_arr:
        s_arr.append(i.product.id)

    for i in range(0,8):
        try:
            m = max(set(s_arr), key=s_arr.count)
            prod_ids.append(m)
            s_arr = [x for x in s_arr if x != m]
        except:
            prod_ids.append(i)
    for i in prod_ids:
        pop_products = addProduct.objects.get(id=i)
        final_list.append(pop_products)

    context = {
        'r':r,
        'final_list':final_list
    }
    return render(request,'index.html',context)

def all(request):
    products = addProduct.objects.all()
    r = request.user
    context = {
        'products': products,
        'r':r
    }
    return render(request,'all.html',context)

def search(request):
    sproducts = addProduct.objects.filter(Category = request.POST.get('re'))
    r = request.user
    p = request.POST.get('re')
    context = {
        'sproducts':sproducts,
        'r':r,
        'p':p
    }
    return render(request,'search.html',context)

def oneProduct(request,id,slug):
    oneP = addProduct.objects.get(id=id,Title=slug)
    alsoLike = addProduct.objects.filter(Category = oneP.Category).exclude(id=id)
    cart_product_form = CartAddProductForm()
    r = request.user
    context = {
        'oneP':oneP,
        'alsoLike':alsoLike,
        'r':r,
        'cart_product_form':cart_product_form
    }
    return render(request,'product.html',context)

def salesPage(request):
    products = addProduct.objects.filter(Discount_Price__isnull= False)
    print(products)
    context = {
        'products':products

    }
    return render(request,'sales.html',context)
def contact(request):
    return render(request,'contact.html')