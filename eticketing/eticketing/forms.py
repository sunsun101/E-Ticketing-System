from django import forms

class IndexForm(forms.Form):
    from_place = forms.CharField(label='From', max_length=100)
    to_place = forms.CharField(label='To', max_length=100)
    date = forms.DateField(label="Date")
    flight_class = forms.CharField(label="Class", max_length=10)
    no_adults = forms.IntegerField(label="Adult")
    no_children = forms.IntegerField(label="Children")
