from django import forms

class ComputadoraFormulario(forms.Form):
    nombre=forms.CharField()
    precio=forms.IntegerField()
    marca=forms.CharField()
    almacenamiento=forms.CharField()
    proveedor=forms.CharField()