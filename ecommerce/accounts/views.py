from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.csrf import csrf_exempt, csrf_protect
# Create your views here.
from accounts.models import Profile
from chat.models import technicalSupportTicket
from orders.admin import OrderAdmin
from .forms import profileForm,userForm
from django.contrib.auth.models import User
from orders.models import order, OrderItem


@csrf_protect
def register(request):
    r = request.user
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/user/login')
    else:
        form = UserCreationForm()
    context = {
        'form':form,
        'r': r
    }
    return render(request, 'register.html', context)

def profile(request,slug):
    r = request.user
    edit = False
    if str(r) == str(slug):
        edit = True

    profileUser = get_object_or_404(Profile,slug=slug)
    context = {
        'pu':profileUser,
        'edit':edit,
        'r':r
    }
    return render(request,'user-profile.html',context)

def edit_profile(request):
    r = request.user
    profileUser = get_object_or_404(Profile, slug=request.user)
    if request.method == 'POST':
        user_form = userForm(request.POST, request.FILES, instance=request.user)
        profile_form = profileForm(request.POST,request.FILES, instance=profileUser)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('/')
    else:
        user_form = userForm(instance=request.user)
        profile_form = profileForm(instance=profileUser)
    context = {
        'user_form':user_form,
        'profile_form':profile_form,
        'r':r
    }
    return render(request,'edit_account.html',context)

def dashboard(request):
    r = request.user
    orders = order.objects.filter(user__username=request.user)
    userinfo = User.objects.get_by_natural_key(username=r)
    profileUser = get_object_or_404(Profile, slug=r)
    open_tickets = len(technicalSupportTicket.objects.filter(user__username = request.user,is_open='True'))
    context = {
        'profileUser':profileUser,
        'userinfo':userinfo,
        'r': r,
        'orders':orders,
        'open_tickets':open_tickets
    }
    return render(request,'my-orders.html',context)

def order_details(request,id):
    r = request.user
    orders = order.objects.get(id=id)
    is_paid = orders.paid
    userinfo = User.objects.get_by_natural_key(username=r)
    profileUser = get_object_or_404(Profile, slug=r)
    open_tickets = len(technicalSupportTicket.objects.filter(user__username=request.user, is_open='True'))
    context = {
        'profileUser': profileUser,
        'userinfo': userinfo,
        'r': r,
        'orders': orders,
        'is_paid':is_paid,
        'open_tickets':open_tickets
    }
    return render(request,'order-detail.html',context)
