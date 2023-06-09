from django import forms
from .models import Clientes


input_css_class = "form-control"
class ClientesForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = ['nombre','telefono','direccion','rns']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class