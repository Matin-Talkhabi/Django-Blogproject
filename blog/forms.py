from django import forms
from .models import Message

class Contact_us_form(forms.Form):

    BIRTH_YEAR_CHOICES = ["1980", "1981", "1982"]

    name = forms.CharField(max_length=10, label='enter your name')
    text = forms.CharField(max_length=10, label='write your text')
    birth = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))


    def clean(self):
        name = self.cleaned_data.get('name')
        text = self.cleaned_data.get('text')
        if name == text:
            raise forms.ValidationError('name and text is same')


class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = '__all__'

