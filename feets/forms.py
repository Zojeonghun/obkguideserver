from django import forms
from django.db.models.query_utils import Q
from . import models

class SearchForm(forms.Form):

    activity = forms.ModelChoiceField(queryset=models.Activity.objects.all())
    waterproof = forms.ModelChoiceField(queryset=models.Waterproof.objects.all())
    hope = forms.ModelChoiceField(queryset=models.Hope.objects.all())
    age = forms.ModelChoiceField(queryset=models.Age.objects.all())


class FeetFilter(forms.Form):
    function = forms.ModelMultipleChoiceField(required=False, queryset=models.Function.objects.all())
    brand = forms.ModelMultipleChoiceField(required=False, queryset=models.Brand.objects.all())
    mobis_grade = forms.ModelMultipleChoiceField(required=False, queryset=models.MobisGrade.objects.all())
    rating = forms.ModelMultipleChoiceField(required=False, queryset=models.Rating.objects.all())
    name = forms.CharField(required=False,)

class FeetAdminForm(forms.ModelForm):
    class Meta:
        model = models.Feet
        fields = [
            'code',
            'name',
            'description',
            'feet_image',
            'mobis_grade',
            'weight',
            'activity',
            'function',
            'age',
            'rating',
            'waterproof',
            'brand',
            'hope',
            'iframe',
            'mass',
            'height',
        ]
