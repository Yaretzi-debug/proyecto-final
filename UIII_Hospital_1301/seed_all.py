
import os
import django
import sys
from datetime import datetime, date

# Add the project path to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UIII_Hospital_1301.backend_Hospital.settings')
django.setup()

from app_Hospital.models import Paciente, Doctor, Sala, Cita, HistorialMedico, Receta, Factura

def seed_all():
    # Pacientes
    pacientes_data = [
        {"nombre": "Ana", "apellido": "García", "fecha_nacimiento": date(1990, 5, 15), "genero": "Femenino", "direccion": "Calle Falsa 123", "telefono": "555-1234", "email": "ana.garcia@example.com", "tipo_sangre": "O+"},
        {"nombre": "Luis", "apellido": "Martínez", "fecha_nacimiento": date(1985, 8, 22), "genero": "Masculino", "direccion": "Avenida Siempreviva 742", "telefono": "555-5678", "email": "luis.martinez@example.com", "tipo_sangre": "A-"}
    ]
    for data in pacientes_data:
        if not Paciente.objects.filter(email=data["email"]).exists():
            Paciente.objects.create(**data)

    # Doctores
    doctores_data = [
        {"nombre": "Carlos", "apellido": "Ruiz", "especialidad": "Cardiología", "telefono": "555-1111", "email": "carlos.ruiz@example.com"},
        {"nombre": "Laura", "apellido": "Jiménez", "especialidad": "Pediatría", "telefono": "555-2222", "email": "laura.jimenez@example.com"}
    ]
    for data in doctores_data:
        if not Doctor.objects.filter(email=data["email"]).exists():
            Doctor.objects.create(**data)

    # Citas
    paciente1 = Paciente.objects.get(email="ana.garcia@example.com")
    doctor1 = Doctor.objects.get(email="carlos.ruiz@example.com")
    sala1 = Sala.objects.get(numero_sala="S-101")
    citas_data = [
        {"paciente": paciente1, "doctor": doctor1, "fecha_hora": datetime(2024, 6, 1, 10, 0, 0), "motivo": "Chequeo anual", "lugar_cita": sala1}
    ]
    for data in citas_data:
        # Simple check to avoid creating the exact same appointment
        if not Cita.objects.filter(paciente=data["paciente"], doctor=data["doctor"], fecha_hora=data["fecha_hora"]).exists():
            Cita.objects.create(**data)

    # HistorialMedico
    paciente2 = Paciente.objects.get(email="luis.martinez@example.com")
    historial_data = {
        "paciente": paciente2,
        "alergias": "Penicilina",
        "enfermedades_cronicas": "Asma",
        "antecedentes_familiares": "Hipertensión"
    }
    if not HistorialMedico.objects.filter(paciente=historial_data["paciente"]).exists():
        HistorialMedico.objects.create(**historial_data)

    # Recetas y Facturas para la primera cita
    cita1 = Cita.objects.first()
    if cita1:
        receta_data = {
            "cita": cita1,
            "medicamento": "Aspirina",
            "dosis": "100mg",
            "instrucciones": "Tomar una vez al día"
        }
        if not Receta.objects.filter(cita=receta_data["cita"], medicamento=receta_data["medicamento"]).exists():
            Receta.objects.create(**receta_data)

        factura_data = {
            "cita": cita1,
            "monto": 75.50,
            "pagada": False
        }
        if not Factura.objects.filter(cita=factura_data["cita"]).exists():
            Factura.objects.create(**factura_data)

    print("¡Se han agregado datos de ejemplo a todas las secciones!")

if __name__ == '__main__':
    seed_all()
