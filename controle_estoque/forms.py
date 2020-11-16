from django import forms


class VendasForm(forms.Form):
    ean = forms.CharField(max_length=13)