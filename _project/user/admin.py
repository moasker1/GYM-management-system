from django.contrib import admin

from .models import Payment, Client, RecentAction, Product


admin.site.register(Payment)
admin.site.register(Client)
admin.site.register(RecentAction)
admin.site.register(Product)