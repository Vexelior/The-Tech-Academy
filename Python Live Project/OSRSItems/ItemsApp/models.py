from django.db import models
from django.contrib.auth.models import User

STYLES = [
    ('N/A', 'N/A'),
    ('Melee', 'Melee'),
    ('Ranged', 'Ranged'),
    ('Magic', 'Magic'),
]

EQUIPMENT_SLOTS = [
    ('N/A', 'N/A'),
    ('Head', 'Head'),
    ('Cape', 'Cape'),
    ('Neck', 'Neck'),
    ('Ammunition', 'Ammunition'),
    ('Weapon', 'Weapon'),
    ('Shield', 'Shield'),
    ('Body', 'Body'),
    ('Legs', 'Legs'),
    ('Hands', 'Hands'),
    ('Feet', 'Feet'),
    ('Ring', 'Ring'),
]


class Item(models.Model):
    # General Information
    type = models.CharField(max_length=20, default="", choices=STYLES )
    name = models.CharField(max_length=20, default="")
    # Attack Bonuses
    atk_stab = models.IntegerField(default=0)
    atk_slash = models.IntegerField(default=0)
    atk_crush = models.IntegerField(default=0)
    atk_magic = models.IntegerField(default=0)
    atk_range = models.IntegerField(default=0)
    # Defence Bonuses
    def_stab = models.IntegerField(default=0)
    def_slash = models.IntegerField(default=0)
    def_crush = models.IntegerField(default=0)
    def_magic = models.IntegerField(default=0)
    def_range = models.IntegerField(default=0)
    # Other Bonuses
    bns_strength = models.IntegerField(default=0)
    bns_range = models.IntegerField(default=0)
    bns_magic = models.IntegerField(default=0)
    bns_prayer = models.IntegerField(default=0)
    # Weapon Slot
    slot = models.CharField(max_length=60, default="", choices=EQUIPMENT_SLOTS)
    # Weapon Speed
    speed = models.IntegerField(default=0)
    # Range
    range = models.IntegerField(default=0)
    # Images
    image = models.URLField(max_length=255, default="")

    # Renaming the models manager to a new variable
    objects = models.Manager()

    def __str__(self):
        return self.name


class Favorites(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.item.name
