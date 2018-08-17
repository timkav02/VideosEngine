from django import forms

class SearchForm(forms.Form):
    query = forms.CharField(max_length=128, widget=forms.TextInput(attrs={'class': "form-control"}),)