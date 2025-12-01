from django import forms  # type: ignore
from app5.models import Register 
class RegisterForm(forms.ModelForm):
    class Meta:
        model=Register 
        fields="__all__"