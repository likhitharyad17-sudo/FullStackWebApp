from django.db import models
from django.urls import reverse

class Car(models.Model):
    MAKE_CHOICES = [
        ('Toyota', 'Toyota'),
        ('Honda', 'Honda'),
        ('Ford', 'Ford'),
        ('Huyndai', 'Huyndai'),
        ('Porsche', 'Porsche'),
        ('Other', 'Other'),
    ]
    make = models.CharField(max_length=50, choices=MAKE_CHOICES)
    model = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField()
    seats = models.PositiveSmallIntegerField(default=4)
    price_per_day = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='cars/', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

    def get_absolute_url(self):
        return reverse('car_detail', args=[str(self.id)])

class Customer(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='bookings')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    total_cost = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def save(self, *args, **kwargs):
        days = (self.end_date - self.start_date).days or 1
        self.total_cost = self.car.price_per_day * days
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Booking {self.car} by {self.customer}"

