from django import forms

from .models import Restaurant, Specialization


class SpecializationForm(forms.ModelForm):
    class Meta:
        model = Specialization
        fields = ('name', )


class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'specialization', 'address', 'website', 'phone')


class SpecChoice(forms.Form):
    spec = [(i, i) for i in Specialization.objects.all()]
    choice = forms.ChoiceField(
        label='Поиск по кухне:',
        choices=spec
    )
