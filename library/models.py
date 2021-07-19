from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

# ============= Book Section =============
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Book(models.Model):

    bookStatus = [
        ("Available", "Available"),
        ("Rented", "Rented"),
        ("Sold", "Sold")
    ]

    author = models.CharField(max_length = 50)
    title = models.CharField(max_length = 200)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, null = True, blank = True)
    rentPerDay = models.DecimalField(max_digits = 4, decimal_places = 2, null = True, blank = True)
    rentPeriod = models.IntegerField(null = True, blank = True)
    active = models.BooleanField(default = True)
    status = models.CharField(max_length = 50, choices=bookStatus, null = True, blank = True)
    category = models.ForeignKey(Category, on_delete = models.PROTECT, null = True, blank = True)
    def __str__(self):
        return self.title