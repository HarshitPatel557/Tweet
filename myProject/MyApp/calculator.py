from django import forms

class Calculator(forms.Form):
    OPS = (
    ("+", "Add"),
    ("-", "Subtract"),
    ("*", "Multiply"),
    ("/", "Divide"),)

    Oprand1=forms.IntegerField()
    Oprator=forms.ChoiceField(choices=OPS)
    Oprand2=forms.CharField()