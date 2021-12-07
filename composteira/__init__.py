from django import forms
class MyForm(forms.ModelForm):
    ...
    def __init__(self, *args, **kwargs):
        super(forms.ComposteiraForms, self).__init__(*args, **kwargs)