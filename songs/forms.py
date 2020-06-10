from django import forms


class TestForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=50)
    # subject = forms.CharField(label='Subject', max_length=50)
    email = forms.EmailField(label='your email', max_length=50, required=False)
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Message'}))
