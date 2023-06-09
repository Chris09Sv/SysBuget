from django import forms
from .models import Facturas


input_css_class = "form-control"
class FacturasForm(forms.ModelForm):
    class Meta:
        model = Facturas
        fields = ['rnc','cliente','combustible','distancia','desde','hasta']



    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = input_css_class