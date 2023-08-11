from django import forms
from .models import Employee, Auto


class WorkerCreationForm(forms.ModelForm):
    # phoneNumber = forms.RegexField(regex=r'^\+?1?\d{9,15}$',
    #                                error_messages = ("Номер телефона должен быть в формате: '+9-999-999-99-99' "), max_length=15)
    class Meta:
        model = Employee
        fields = ['firstName','lastName','middleName','phoneNumber','adress','department']

class AutoCreationForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = ['user','model','avto_nomer','vin','year_manufacture', 'chassis', 'engine_power', 'tech_inspection', 'mileage', 'average_fuel_use', 'type']
