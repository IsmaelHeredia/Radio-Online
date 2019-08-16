# Written By Ismael Heredia in the year 2017

from django import forms

from app.models import Genero,Emisora

class GeneroForm(forms.ModelForm):
    
    class Meta:
        
        model = Genero

        fields = [
            'nombre',
        ]

        labels = {
            'nombre':'Nombre',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre de categoria','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
        }

class EmisoraForm(forms.ModelForm):

    class Meta:
        
        model = Emisora

        fields = [
            'nombre',
            'url',
            'genero',
        ]

        labels = {
            'nombre':'Nombre',
            'url':'URL',
            'genero':'Genero',
        }

        widgets = {
            'nombre':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese nombre','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'url':forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese URL','autocomplete':'off','autocorrect':'off','spellcheck':'false'}),
            'genero':forms.Select(attrs={'class':'form-control'}),        
        }