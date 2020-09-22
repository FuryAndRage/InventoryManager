from django import forms
from .models import WithdrawalProduct

class WithdrawalForm(forms.ModelForm):
    class Meta:
        model = WithdrawalProduct
        fields = '__all__'
        widgets = {'user':forms.HiddenInput()}