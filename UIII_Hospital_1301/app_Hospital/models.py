from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    genero = models.CharField(max_length=10)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    tipo_sangre = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Dr. {self.nombre} {self.apellido} - {self.especialidad}"

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f"Cita de {self.paciente} con {self.doctor} el {self.fecha_hora}"

class HistorialMedico(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.CASCADE)
    alergias = models.TextField(blank=True)
    enfermedades_cronicas = models.TextField(blank=True)
    antecedentes_familiares = models.TextField(blank=True)

    def __str__(self):
        return f"Historial Médico de {self.paciente}"

class Receta(models.Model):
    cita = models.ForeignKey(Cita, on_delete=models.CASCADE)
    medicamento = models.CharField(max_length=100)
    dosis = models.CharField(max_length=100)
    instrucciones = models.TextField()

    def __str__(self):
        return f"Receta para {self.cita.paciente} - {self.medicamento}"

class Factura(models.Model):
    cita = models.OneToOneField(Cita, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    pagada = models.BooleanField(default=False)

    def __str__(self):
        return f"Factura para {self.cita.paciente} - Monto: {self.monto}"
