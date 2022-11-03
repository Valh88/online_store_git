from django import forms


class AddReviewForm(forms.Form):
    review = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-textarea',
                                                          'placeholder': 'Review',
                                                          'type': 'text'}), label='')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input',
                                                         'type': 'text',
                                                         'placeholder': 'name'}), label='')
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-input',
                                                          'type': 'text',
                                                          'placeholder': 'Email'}), label='')
