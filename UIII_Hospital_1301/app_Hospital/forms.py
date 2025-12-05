from django import forms
from .models import HistorialMedico, Receta, Factura

class HistorialMedicoForm(forms.ModelForm):
    class Meta:
        model = HistorialMedico
        fields = ['paciente', 'alergias', 'enfermedades_cronicas', 'antecedentes_familiares']

class RecetaForm(forms.ModelForm):
    class Meta:
        model = Receta
        fields = ['cita', 'medicamento', 'dosis', 'instrucciones']

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Factura
        fields = ['cita', 'monto', 'pagada']
