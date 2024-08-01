from django.db import models
from django.utils import timezone
from django.db.models import Sum
from decimal import Decimal
from django.contrib.auth.models import User

# ===============================================================================================
class Client(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    phone = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateTimeField( blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    
    @property
    def rest(self):
        total_sales = self.sale_set.aggregate(models.Sum('total'))['total__sum'] or 0
        total_payments = self.payment_set.aggregate(models.Sum('paid_money'))['paid_money__sum'] or 0

        return (self.opening_balance + total_sales) - total_payments

# ===============================================================================================
class Product(models.Model):
    name = models.CharField(max_length=100,blank=True, null=True)
    num = models.PositiveIntegerField(blank=True, null=True)
    price = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
# ===============================================================================================
class Payment(models.Model):
    lose = models.CharField(max_length=100,blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)
    paid_money = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
# ===============================================================================================
class RecentAction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100,blank=True, null=True)  
    action_sort = models.CharField(max_length=100,blank=True, null=True)  
    model_affected = models.CharField(max_length=100,blank=True, null=True)  
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
# ===============================================================================================

