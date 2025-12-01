from django.contrib import admin
from .models import Car, Customer, Booking

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('make','model','year','price_per_day','available')

admin.site.register(Customer)
admin.site.register(Booking)
