from django import forms

class BuscarMoto(forms.Form):
    marca = forms.CharField(max_length=20, required=False)