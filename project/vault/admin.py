from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

# Register your models here.

#  user, country, state, city, 
# user_table, item_categ, item, prod_cart, 
# order, payment, feedback, contact_us

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'date_joined')
    search_fields = ('name',)
    
    
@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

    

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
  
    
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
    
@admin.register(User_table)
class User_table_Admin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address', 'phone_no', 'image_tag')
    search_fields = ('user',)
    list_per_page = 10
    
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px" />')
        return "No Image"
    image_tag.short_description = 'Image'
    
    
@admin.register(Item_category)
class Item_category_Admin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'desc', 'category', 'price', 'condition', 'image_tag', 'upload_date')
    search_fields = ('name',)
    list_per_page = 10
    list_filter = ['category',]
    list_editable = ('category',)
    
    def image_tag(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="100px" />')
        return "No Image"
    image_tag.short_description = 'Image'
    
    
@admin.register(Prod_cart)
class Prod_cart_Admin(admin.ModelAdmin):
    list_display = ('user', 'item', 'price', 'quantity', 'order_id', 'order_status')
    search_fields = ('item',)
    list_editable = ('quantity',)
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'quantity', 'total_price', 'order_date', 'shipping_address', 'delivery_date', 'status')
    list_per_page = 10
    list_filter = ['status',]
    search_fields = ('name',)
    
    
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'order', 'amt', 'payment_mode', 'payment_status', 'payment_date')
    list_filter = ['payment_status',]
    
    
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('user', 'item', 'rating', 'comment', 'review_date')
    search_fields = ('user', 'item')
    list_editable = ('rating',)
    list_filter = ['rating',]
    
    
@admin.register(Conatact_us_table)
class Contact_us_Admin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'phone', 'created_at')
    search_fields = ('name', 'subject')
    list_editable = ('message',)
    
