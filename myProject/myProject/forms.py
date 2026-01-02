from django import forms

class UsersForm(forms.Form):
    val1 = forms.CharField(label="Num1")
    val2 = forms.CharField(label="Num2")
    
