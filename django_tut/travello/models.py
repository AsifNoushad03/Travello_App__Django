from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    duration = models.IntegerField()

    def __str__(self):
        return self.name

class Booking(models.Model):
     name = models.ForeignKey(Destination,on_delete=models.CASCADE)
     full_name = models.CharField(max_length=100)
     p_phone = models.CharField(max_length=10)
     depart_date = models.DateField()
     return_date = models.DateField()
     booked_on = models.DateField(auto_now=True)

  



