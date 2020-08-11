from django import forms

class New_Title(forms.Form):
    title   = forms.CharField(label='',widget=forms.TextInput(
        attrs={
            "placeholder":"Title of Entry"
            }
        ))
    

class New_Content(forms.Form):
    content = forms.CharField(label='', widget=forms.Textarea(
        attrs={
            "placeholder":"Content"
        }
    ))
