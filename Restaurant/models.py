from django.db import models

# Create your models here.

class BookingTable(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateField()
class MenuTable(models.Model):
    Title = models.CharField(max_length=255)
    price  = models.DecimalField(max_digits=10,decimal_places=2)
    Inventory = models.IntegerField
    def get_item(self):
        return f'{self.Title} : {str(self.price)}'
