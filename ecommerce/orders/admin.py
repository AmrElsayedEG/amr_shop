from django.contrib import admin
from .models import OrderItem,order
# Register your models here.
class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','user','first_name','last_name','address','email','city','postal_code','paid',)
    list_filter = ('paid','created','updated',)
    search_fields = ['first_name','last_name','email']
    inlines = [OrderItemAdmin,]



admin.site.register(order,OrderAdmin)