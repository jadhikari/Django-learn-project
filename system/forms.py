from django import forms

class usersForm(forms.Form):
    num1=forms.CharField(label='Name',widget=forms.TextInput(attrs={'class':"form-control"}))
    num2=forms.CharField(label='NAME 2',widget=forms.TextInput(attrs={'class':"form-control"}))
    num3=forms.CharField(label='NAME 3',widget=forms.TextInput(attrs={'class':"form-control"}))
    num4=forms.CharField(label='NAME 4',widget=forms.TextInput(attrs={'class':"form-control"}))