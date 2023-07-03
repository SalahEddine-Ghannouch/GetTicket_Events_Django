from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Cart(models.Model):
    eventName = models.CharField(max_length=255)
    price =  models.DecimalField(max_digits=8, decimal_places=2,null=True)
    quantity = models.IntegerField()
    start_Date = models.DateTimeField()
    Date_Added = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    Event_Attendet = models.CharField(max_length=255)

'''
class Order(models.Model):
    EventAttendet = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    TransactionId = models.CharField(max_length=50, null=True)

    @property
    def get_cart_total(self):
        Oritems = self.orderitem_set.all()
        total = sum([item.get_total for item in Oritems])
        return total
    
    @property
    def get_cart_items(self):
        Oritems = self.orderitem_set.all()
        total = sum([item.quantity for item in Oritems])
        return total
    

class OrderItem(models.Model):
    #This line bellow has changed
    #event = models.ForeignKey(Event , on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order , on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        toal = self.quantity * self.quantity
        return toal
'''