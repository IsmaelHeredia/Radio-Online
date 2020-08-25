# Written By Ismael Heredia in the year 2020

from django import forms

from app.models import Emisora

class EmisoraForm(forms.ModelForm):

    class Meta:
        
        model = Emisora

        fields = [
            'nombre',
            'url',
            'generos',
        ]

        labels = {
            'nombre':'Nombre',
            'url':'URL',
            'generos':'Géneros',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'url':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese URL','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'generos':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese géneros','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),        
        }