from django import forms
from .models import HistorialMedico, Receta, Factura, Cita, Sala

class CitaForm(forms.ModelForm):
    lugar_cita = forms.ModelChoiceField(queryset=Sala.objects.all(), label="Lugar de la Cita")
    fecha_hora = forms.DateTimeField(
        widget=forms.DateTimeInput(format='%Y-%m-%dT%H:%M', attrs={'type': 'datetime-local'}),
        label="Fecha y Hora"
    )
    class Meta:
        model = Cita
        fields = ['paciente', 'doctor', 'fecha_hora', 'motivo', 'tipo_cita', 'lugar_cita', 'duracion_estimada', 'tipo_servicio', 'codigo_cita', 'prioridad', 'notas_adicionales']

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'numero_sala', 'area', 'capacidad', 'tipo', 'disponibilidad', 'ubicacion', 'descripcion', 'equipamiento', 'estado_mantenimiento', 'nivel_seguridad', 'observaciones']

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
