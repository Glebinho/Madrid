from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import  History
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, DateInput, Select
class HistForm(ModelForm):
    class Meta:
        model=History
        fields=['tovar','razmer','kol','email','fio','date','text']

widgets = {
"tovar": Select(attrs={
'class': 'form-control',
}),
"razmer": Select(attrs={
'class': 'form-control',
}),
"kol": TextInput(attrs={
'class': 'form-control',
}),
"email": TextInput(attrs={
'class': 'form-control',
}),
"fio": TextInput(attrs={
'class': 'form-control',
}),
"date": DateTimeInput(attrs={
'class': 'form-control',
}),
"text": Textarea(attrs={
'class': 'form-control',
}),
}