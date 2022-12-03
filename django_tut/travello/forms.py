from django import  forms
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'depart_date' : DateInput(),
            'return_date' : DateInput()
        }

        labels ={
            'full_name':'Full Name',
            'name' : "Destination  Name",
            'p_phone' : "Phone Number ",
            'p_email' : "Patient Email",
            'depart_date' : "Depart Date",
        }
