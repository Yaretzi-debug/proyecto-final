
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
    # Pacientes - Using update_or_create to avoid duplicates and preserve IDs
    pacientes_data = [
        {"nombre": "Luis", "apellido": "Martínez", "fecha_nacimiento": date(1985, 8, 22), "genero": "Masculino", "direccion": "Avenida Siempreviva 742", "telefono": "555-5678", "email": "luis.martinez@example.com", "tipo_sangre": "A-"},
        {"nombre": "Maria", "apellido": "Lopez", "fecha_nacimiento": date(1992, 3, 10), "genero": "Femenino", "direccion": "Calle Luna 456", "telefono": "555-8765", "email": "maria.lopez@example.com", "tipo_sangre": "B+"},
        {"nombre": "Carlos", "apellido": "Sanchez", "fecha_nacimiento": date(1980, 11, 5), "genero": "Masculino", "direccion": "Calle Sol 789", "telefono": "555-4321", "email": "carlos.sanchez@example.com", "tipo_sangre": "AB+"},
        {"nombre": "Laura", "apellido": "Gomez", "fecha_nacimiento": date(1995, 7, 20), "genero": "Femenino", "direccion": "Avenida Estrella 101", "telefono": "555-9876", "email": "laura.gomez@example.com", "tipo_sangre": "O-"}
    ]
    for data in pacientes_data:
        Paciente.objects.update_or_create(email=data['email'], defaults=data)

    # Doctores
    doctores_data = [
        {"nombre": "Carlos", "apellido": "Ruiz", "especialidad": "Cardiología", "telefono": "555-1111", "email": "carlos.ruiz@example.com"},
        {"nombre": "Laura", "apellido": "Jiménez", "especialidad": "Pediatría", "telefono": "555-2222", "email": "laura.jimenez@example.com"},
        {"nombre": "Ana", "apellido": "García", "especialidad": "Dermatología", "telefono": "555-3333", "email": "ana.garcia@example.com"},
        {"nombre": "Juan", "apellido": "Pérez", "especialidad": "Neurología", "telefono": "555-4444", "email": "juan.perez@example.com"}
    ]
    for data in doctores_data:
        Doctor.objects.update_or_create(email=data['email'], defaults=data)

    # Salas
    salas_data = [
        {"nombre": "Sala de Consulta 1", "numero_sala": "S-101", "area": "Cardiología", "capacidad": 1, "tipo": "Consulta", "disponibilidad": True, "ubicacion": "Piso 1", "descripcion": "Sala para consultas generales de cardiología.", "equipamiento": "ECG, Camilla", "estado_mantenimiento": "bueno", "nivel_seguridad": "Bajo", "observaciones": ""},
        {"nombre": "Sala de Pediatría 1", "numero_sala": "S-102", "area": "Pediatría", "capacidad": 1, "tipo": "Consulta", "disponibilidad": True, "ubicacion": "Piso 1", "descripcion": "Sala para consultas pediátricas.", "equipamiento": "Camilla Pediátrica, Juguetes", "estado_mantenimiento": "bueno", "nivel_seguridad": "Bajo", "observaciones": ""}
    ]
    for data in salas_data:
        Sala.objects.update_or_create(numero_sala=data['numero_sala'], defaults=data)

    # Get objects that are guaranteed to exist now
    paciente_luis = Paciente.objects.get(email="luis.martinez@example.com")
    paciente_maria = Paciente.objects.get(email="maria.lopez@example.com")
    doctor_ruiz = Doctor.objects.get(email="carlos.ruiz@example.com")
    doctor_jimenez = Doctor.objects.get(email="laura.jimenez@example.com")
    sala_101 = Sala.objects.get(numero_sala="S-101")
    sala_102 = Sala.objects.get(numero_sala="S-102")

    # Citas
    cita_luis, _ = Cita.objects.update_or_create(codigo_cita="CITA-001", defaults={"paciente": paciente_luis, "doctor": doctor_ruiz, "fecha_hora": datetime(2024, 6, 10, 9, 0, 0), "motivo": "Dolor de pecho", "tipo_servicio": "Cardiología", "lugar_cita": sala_101, "notas_adicionales": "El paciente reporta dolor intermitente."})
    cita_maria, _ = Cita.objects.update_or_create(codigo_cita="CITA-002", defaults={"paciente": paciente_maria, "doctor": doctor_jimenez, "fecha_hora": datetime(2024, 6, 10, 11, 0, 0), "motivo": "Vacunación", "tipo_servicio": "Pediatría", "lugar_cita": sala_102, "notas_adicionales": "Vacuna de los 2 años."})

    # HistorialMedico
    HistorialMedico.objects.update_or_create(paciente=paciente_luis, defaults={"alergias": "Ninguna conocida", "enfermedades_cronicas": "Hipertensión", "antecedentes_familiares": "Enfermedad cardíaca"})
    HistorialMedico.objects.update_or_create(paciente=paciente_maria, defaults={"alergias": "Polen", "enfermedades_cronicas": "Asma", "antecedentes_familiares": "Ninguno"})

    # Recetas
    Receta.objects.update_or_create(cita=cita_luis, medicamento="Aspirina", defaults={"dosis": "100mg", "instrucciones": "Tomar con alimentos."})
    Receta.objects.update_or_create(cita=cita_maria, medicamento="Paracetamol", defaults={"dosis": "10mg/kg", "instrucciones": "En caso de fiebre o dolor."})

    # Facturas
    Factura.objects.update_or_create(cita=cita_luis, defaults={"monto": 150.00, "pagada": True})
    Factura.objects.update_or_create(cita=cita_maria, defaults={"monto": 50.00, "pagada": True})

    print("¡Los datos de ejemplo han sido creados o actualizados!")

if __name__ == '__main__':
    seed_all()
