from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escribe un titulo'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Escribe una descripcion'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'}),
        }