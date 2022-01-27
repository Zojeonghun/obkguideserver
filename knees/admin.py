from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.MobisGrade)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Activity)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Function)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Age)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Hope)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Brand)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Rating)
class CustomUserAdmin(admin.ModelAdmin):
    pass

@admin.register(models.Waterproof)
class CustomUserAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Knee)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("code", "name", 'pk', 'height', 'mass',)
    list_filter = (
            "mobis_grade",
            "activity",
            'function',
            'age',
            'hope',
            'brand',
            'rating',
            'waterproof'
            )
    filter_horizontal = (
        "mobis_grade",
        "activity", 
        'function', 
        'age', 
        'hope', 
        'brand',
        'rating',
        'waterproof',
        )