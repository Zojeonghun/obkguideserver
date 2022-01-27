from django.db import models
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ManyToManyField

# Create your models here.

class AbstractItem(models.Model):
    name = models.CharField(max_length=50, default="", blank=True)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name

class MobisGrade(AbstractItem):
    pass

class Activity(AbstractItem):
    pass

class Function(AbstractItem):
    pass

class Age(AbstractItem):
    pass

class Hope(AbstractItem):
    pass

class Brand(AbstractItem):
    pass

class Rating(AbstractItem):
    pass

class Waterproof(AbstractItem):
    pass

class Knee(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    knee_image = models.ImageField(upload_to='knees',blank=True, null=True)
    mobis_grade = models.ManyToManyField(MobisGrade, related_name="knees", blank=True)
    weight = models.CharField(max_length=50, blank=True)
    activity = models.ManyToManyField(Activity, related_name='knees', blank=True)
    function = models.ManyToManyField(Function, related_name='knees', blank=True)
    age = models.ManyToManyField(Age, related_name='knees', blank=True)
    hope = models.ManyToManyField(Hope, related_name='knees', blank=True)
    brand = models.ManyToManyField(Brand, related_name='knees', blank=True)
    rating = models.ManyToManyField(Rating, related_name='knees', blank=True)
    waterproof = models.ManyToManyField(Waterproof, related_name='knees', blank=True)
    iframe = models.TextField(blank=True)
    mass = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name