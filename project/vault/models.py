from django.db import models

# Create your models here.

condition = [
    ('Bad', 'Bad'),
    ('Good', 'Good'),
    ('Best', 'Best'),
]

order_status = [
    ('Pending', 'Pending'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
]
payment_method = [
    ('credit_card', 'Credit Card'),
    ('debit_card', 'Debit Card'),
    ('paypal', 'PayPal'),
    ('other', 'Other'),
]

payment_status = [
    ('pending', 'Pending'),
    ('completed', 'Completed'),
    ('failed', 'Failed'),
]

rating_choices = [
    (i, f'{i}') for i in range(1, 6)
]

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=20)
    date_joined = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    
    
class Country(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    

class State(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    
class User_table(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dob = models.DateField(auto_now_add=True)
    address = models.TextField()
    phone_no = models.CharField(max_length=20)
    image = models.ImageField(upload_to='user-img/', blank=True, null=True)
    

class Item_category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Item(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    desc = models.TextField()
    category = models.ForeignKey(Item_category, on_delete=models.CASCADE)
    price = models.CharField(max_length=20)
    condition = models.CharField(max_length=100, choices=condition)
    upload_date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='item-img/')
    
    def __str__(self):
        return self.name
    
    
class Prod_cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    price = models.CharField(max_length=20)
    quantity = models.IntegerField(default=0)
    order_id = models.CharField(max_length=200)
    order_status = models.CharField(max_length=100, choices=order_status)


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    total_price = models.CharField(max_length=100)
    order_date = models.DateField(auto_now_add=True)
    shipping_address = models.TextField()
    delivery_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100, choices=order_status, default='pending')
    
    
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    amt = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=100, choices=payment_method)
    payment_status = models.CharField(max_length=100, choices=payment_status, default='pending')
    payment_date = models.DateField(auto_now_add=True)
    

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=rating_choices, default=5)
    comment = models.TextField()
    review_date = models.DateField(auto_now_add=True)
    

class Conatact_us_table(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=False)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    phone = models.CharField(max_length=20)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name