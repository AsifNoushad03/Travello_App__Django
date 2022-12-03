from django.shortcuts import render
from .models import Destination,Booking
from .forms import BookingForm

# Create your views here.
def index(request):
    dests = Destination.objects.all()
    return render(request,'index.html',{'dests': dests})


    

def booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'confirmation.html')
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request,'booking.html',dict_form)


