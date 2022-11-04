from django import forms


DELIVERY_CHOICES = [
    ('ordinary', 'ordinary'),
    ('express', 'express'),
]

PAY_CHOICES = [
    ('online', 'online'),
    ('someone', 'someone'),
]


class OrderForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=12)
    mail = forms.EmailField()
    delivery = forms.MultipleChoiceField(required=False,
                                         widget=forms.CheckboxSelectMultiple,
                                         choices=DELIVERY_CHOICES,
                                         )
    city = forms.CharField(max_length=10)
    address = forms.CharField(max_length=100)
    pay = forms.MultipleChoiceField(required=False,
                                    widget=forms.CheckboxSelectMultiple,
                                    choices=PAY_CHOICES,
                                    )


class PaymentForm(forms.Form):
    num_card = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input Payment-bill',
                                                             'id': 'numero1',
                                                             'name': 'numero1',
                                                             'type': 'text',
                                                             'placeholder': '9999 9999',
                                                             'data-mask': '9999 9999',
                                                             'data-validate': 'require pay'}))
    order = forms.IntegerField(widget=forms.HiddenInput)
