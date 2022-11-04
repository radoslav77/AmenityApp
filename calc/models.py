from datetime import datetime
from pickle import TRUE
from django.db import models
from django.db.models import Model
from datetime import timedelta
import datetime


# Create your models here.

FRUIT = {
    ('Large fruit', 'Large fruit'),
    ('Midium fruit', 'Midium fruit'),
    ('Small fruit', 'Small fruit'),
    ('Presidential', 'Presidential')
}

DRINK = {
    ('White wine', 'White wine'),
    ('Red wine', 'Red wine'),
    ('Champagne', 'Champagne'),
    ('Negroni', 'Negroni'),
    ('Water', 'Water')
}

TURN_DOWN = {
    ('Florentine', 'Florebntine'),
    ('Macaroons', 'Macaroons'),
    ('Pistachio Finnacier', 'Pistachio Finnacier'),
    ('Madleines', 'Madleines'),
    ('Flapjack','Flapjack'),
    ('Lemon cake', 'Lemon cake')

}

DESSERT = {
    ('Chocolate truffle', 'Chocolate truffle'),
    ('Macaroons 4pcs', 'Macaroons 4pcs'),
    ('Macaroons 8pcs', 'Macaroons 8pcs'),
    ('Baklava', 'Baklava'),
    ('Maamul', 'Maamul'),
    ('Arab amenity', 'Arab amenity'),

}

BIRTHDAY = {
    ('Happy Birthday', 'Happy Birthday'),
    ('Happy Aniversary', 'Happy Amiversary'),
    ('Congartulations', 'Congratulations')
}

MONTHS = {
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('Octomber', 'Octomber'),
    ('November', 'November'),
    ('December', 'December')
}



class InputAmenity(models.Model):
    big_id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300)
    membership = models.CharField(max_length=400)
    arrival_date = models.CharField(max_length=100)
    returns = models.IntegerField(default=0)
    vip_level = models.IntegerField(default=0)
    guests_count = models.IntegerField(default=1)
    room_allocation = models.IntegerField(default=100)
    num_of_fruit = models.IntegerField(default=1, blank=True, null=True)
    fruit_amenity = models.CharField(
        max_length=200, choices=FRUIT, blank=True, null=True)
    num_of_drink = models.IntegerField(default=0, blank=True, null=True)
    drink_amenity = models.CharField(
        max_length=200, choices=DRINK, blank=True, null=True)
    num_of_dessert = models.IntegerField(default=1, blank=True, null=True)
    dessert_amenity = models.CharField(
        max_length=200, choices=DESSERT, blank=True, null=True)
    birthday_amenity = models.CharField(
        max_length=200, choices=BIRTHDAY, blank=True, null=True)
    month = models.CharField(max_length=300, choices=MONTHS)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name, self.arrival_date, self.month}'


class LongStay(models.Model):
    title = models.ForeignKey(InputAmenity, on_delete=models.CASCADE)
    drink_amenity = models.CharField(
        max_length=200, choices=DRINK, blank=True, null=True)
    amenity = models.CharField(max_length=200, choices=TURN_DOWN)
    month = models.CharField(max_length=300, choices=MONTHS)
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title, self.date}'