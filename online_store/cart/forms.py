from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.CharField(initial=1, label='',
                               widget=forms.TextInput(attrs={'class': 'Amount-input form-input',
                                                             'type': 'text',
                                                             'id': 'quantity'}))
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput(attrs={'id': 'update'}))
