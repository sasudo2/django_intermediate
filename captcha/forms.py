from .models import verified
from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox 

class verify_form(forms.ModelForm):
    class Meta:
        model = verified
        fields = ['name', 'email']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'id': 'title', 'placeholder': 'Task title'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'id': 'email', 'placeholder': 'example@eg.com'})
        }
    captcha = ReCaptchaField(widget = ReCaptchaV2Checkbox)