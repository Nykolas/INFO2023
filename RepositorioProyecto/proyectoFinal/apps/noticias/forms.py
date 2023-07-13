from django import forms
from .models import Noticia


class Form_Alta(forms.ModelForm):

    class Meta:
        model = Noticia
        fields = ('titulo','contenido','imagen','categoria')

        
        