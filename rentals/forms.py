from django import forms
from .models import Booking, Customer

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type':'date'}),
            'end_date': forms.DateInput(attrs={'type':'date'}),
        }
