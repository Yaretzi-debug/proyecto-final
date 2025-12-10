
import os
import django
import sys

# Add the project path to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UIII_Hospital_1301.backend_Hospital.settings')

django.setup()

from app_Hospital.models import Sala

def seed_salas():
    # Clear existing data to avoid duplicates
    Sala.objects.all().delete()

    salas_data = [
        {
            "nombre": "Sala de Cirugía 1",
            "numero_sala": "S-101",
            "area": "Quirófanos",
            "capacidad": 15,
            "tipo": "Quirófano",
            "disponibilidad": True,
            "ubicacion": "Piso 1, Ala Oeste",
            "descripcion": "Sala de cirugía general equipada para procedimientos mayores.",
            "equipamiento": "Mesa de operaciones, monitor de signos vitales, lámpara quirúrgica, equipo de anestesia.",
            "estado_mantenimiento": "bueno",
            "nivel_seguridad": "Alto",
            "observaciones": "Esterilización completada el día de hoy."
        },
        {
            "nombre": "Sala de Recuperación A",
            "numero_sala": "R-201",
            "area": "Postoperatorio",
            "capacidad": 8,
            "tipo": "Recuperación",
            "disponibilidad": True,
            "ubicacion": "Piso 2, Ala Este",
            "descripcion": "Sala para la recuperación de pacientes después de una cirugía.",
            "equipamiento": "Camas hospitalarias, monitores de signos vitales, bombas de infusión.",
            "estado_mantenimiento": "bueno",
            "nivel_seguridad": "Medio",
            "observaciones": "Ocupación actual: 3 pacientes."
        },
        {
            "nombre": "Consultorio Pediátrico 3",
            "numero_sala": "C-303",
            "area": "Pediatría",
            "capacidad": 4,
            "tipo": "Consultorio",
            "disponibilidad": False,
            "ubicacion": "Piso 3, Ala Norte",
            "descripcion": "Consultorio para atención ambulatoria de pacientes pediátricos.",
            "equipamiento": "Escritorio, camilla de examinación pediátrica, balanza para bebés, otoscopio.",
            "estado_mantenimiento": "regular",
            "nivel_seguridad": "Bajo",
            "observaciones": "El monitor de presión no funciona correctamente."
        },
        {
            "nombre": "Sala de Radiología 2",
            "numero_sala": "X-002",
            "area": "Imagenología",
            "capacidad": 1,
            "tipo": "Rayos X",
            "disponibilidad": True,
            "ubicacion": "Planta Baja, Ala Sur",
            "descripcion": "Sala equipada para tomar radiografías.",
            "equipamiento": "Máquina de Rayos X, panel de control, delantales de plomo.",
            "estado_mantenimiento": "bueno",
            "nivel_seguridad": "Alto",
            "observaciones": ""
        }
    ]

    for data in salas_data:
        Sala.objects.create(**data)

    print("¡Se han agregado datos de ejemplo a las salas!")

if __name__ == '__main__':
    seed_salas()
