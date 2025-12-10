from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Doctor, Cita, HistorialMedico, Receta, Factura, Sala
from .forms import HistorialMedicoForm, RecetaForm, FacturaForm, CitaForm, SalaForm
from django.views.decorators.csrf import csrf_protect

def inicio_hospital(request):
    return render(request, 'inicio.html')

# Vistas de Paciente
def agregar_paciente(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        fecha_nacimiento = request.POST['fecha_nacimiento']
        genero = request.POST['genero']
        direccion = request.POST['direccion']
        telefono = request.POST['telefono']
        email = request.POST['email']
        tipo_sangre = request.POST['tipo_sangre']
        
        paciente = Paciente(nombre=nombre, apellido=apellido, fecha_nacimiento=fecha_nacimiento, genero=genero, direccion=direccion, telefono=telefono, email=email, tipo_sangre=tipo_sangre)
        paciente.save()
        return redirect('ver_pacientes')
    return render(request, 'paciente/agregar_paciente.html')

def ver_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'paciente/ver_pacientes.html', {'pacientes': pacientes})

def actualizar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'paciente/actualizar_paciente.html', {'paciente': paciente})

def realizar_actualizacion_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.nombre = request.POST['nombre']
        paciente.apellido = request.POST['apellido']
        paciente.fecha_nacimiento = request.POST['fecha_nacimiento']
        paciente.genero = request.POST['genero']
        paciente.direccion = request.POST['direccion']
        paciente.telefono = request.POST['telefono']
        paciente.email = request.POST['email']
        paciente.tipo_sangre = request.POST['tipo_sangre']
        paciente.save()
        return redirect('ver_pacientes')
    return render(request, 'paciente/actualizar_paciente.html', {'paciente': paciente})

@csrf_protect
def borrar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ver_pacientes')
    return render(request, 'paciente/borrar_paciente.html', {'paciente': paciente})

# Vistas de Doctor
def agregar_doctor(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        especialidad = request.POST['especialidad']
        telefono = request.POST['telefono']
        email = request.POST['email']
        
        doctor = Doctor(nombre=nombre, apellido=apellido, especialidad=especialidad, telefono=telefono, email=email)
        doctor.save()
        return redirect('ver_doctores')
    return render(request, 'doctor/agregar_doctor.html')

def ver_doctores(request):
    doctores = Doctor.objects.all()
    return render(request, 'doctor/ver_doctores.html', {'doctores': doctores})

def actualizar_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    return render(request, 'doctor/actualizar_doctor.html', {'doctor': doctor})

def realizar_actualizacion_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        doctor.nombre = request.POST['nombre']
        doctor.apellido = request.POST['apellido']
        doctor.especialidad = request.POST['especialidad']
        doctor.telefono = request.POST['telefono']
        doctor.email = request.POST['email']
        doctor.save()
        return redirect('ver_doctores')
    return render(request, 'doctor/actualizar_doctor.html', {'doctor': doctor})

@csrf_protect
def borrar_doctor(request, doctor_id):
    doctor = get_object_or_404(Doctor, id=doctor_id)
    if request.method == 'POST':
        doctor.delete()
        return redirect('ver_doctores')
    return render(request, 'doctor/borrar_doctor.html', {'doctor': doctor})

# Vistas de Cita
def agregar_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_citas')
    else:
        form = CitaForm()
    return render(request, 'cita/agregar_cita.html', {'form': form})

def ver_citas(request):
    citas = Cita.objects.all()
    return render(request, 'cita/ver_citas.html', {'citas': citas})

def actualizar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    form = CitaForm(instance=cita)
    return render(request, 'cita/actualizar_cita.html', {'form': form, 'cita': cita})

def realizar_actualizacion_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('ver_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'cita/actualizar_cita.html', {'form': form, 'cita': cita})

@csrf_protect
def borrar_cita(request, cita_id):
    cita = get_object_or_404(Cita, id=cita_id)
    if request.method == 'POST':
        cita.delete()
        return redirect('ver_citas')
    return render(request, 'cita/borrar_cita.html', {'cita': cita})

# Vistas de Sala
def agregar_sala(request):
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_salas')
    else:
        form = SalaForm()
    return render(request, 'sala/agregar_sala.html', {'form': form})

def ver_salas(request):
    salas = Sala.objects.all()
    return render(request, 'sala/ver_salas.html', {'salas': salas})

def actualizar_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    form = SalaForm(instance=sala)
    return render(request, 'sala/actualizar_sala.html', {'form': form, 'sala': sala})

def realizar_actualizacion_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            form.save()
            return redirect('ver_salas')
    else:
        form = SalaForm(instance=sala)
    return render(request, 'sala/actualizar_sala.html', {'form': form, 'sala': sala})

@csrf_protect
def borrar_sala(request, sala_id):
    sala = get_object_or_404(Sala, id=sala_id)
    if request.method == 'POST':
        sala.delete()
        return redirect('ver_salas')
    return render(request, 'sala/borrar_sala.html', {'sala': sala})

# Vistas de Historial Medico
def agregar_historial(request):
    if request.method == 'POST':
        form = HistorialMedicoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_historiales')
    else:
        form = HistorialMedicoForm()
    return render(request, 'historial/agregar_historial.html', {'form': form})

def ver_historiales(request):
    historiales = HistorialMedico.objects.all()
    return render(request, 'historial/ver_historiales.html', {'historiales': historiales})

def actualizar_historial(request, historial_id):
    historial = get_object_or_404(HistorialMedico, id=historial_id)
    form = HistorialMedicoForm(instance=historial)
    return render(request, 'historial/actualizar_historial.html', {'form': form, 'historial': historial})

def realizar_actualizacion_historial(request, historial_id):
    historial = get_object_or_404(HistorialMedico, id=historial_id)
    if request.method == 'POST':
        form = HistorialMedicoForm(request.POST, instance=historial)
        if form.is_valid():
            form.save()
            return redirect('ver_historiales')
    else:
        form = HistorialMedicoForm(instance=historial)
    return render(request, 'historial/actualizar_historial.html', {'form': form, 'historial': historial})

@csrf_protect
def borrar_historial(request, historial_id):
    historial = get_object_or_404(HistorialMedico, id=historial_id)
    if request.method == 'POST':
        historial.delete()
        return redirect('ver_historiales')
    return render(request, 'historial/borrar_historial.html', {'historial': historial})

# Vistas de Receta
def agregar_receta(request):
    if request.method == 'POST':
        form = RecetaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_recetas')
    else:
        form = RecetaForm()
    return render(request, 'receta/agregar_receta.html', {'form': form})

def ver_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'receta/ver_recetas.html', {'recetas': recetas})

def actualizar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    form = RecetaForm(instance=receta)
    return render(request, 'receta/actualizar_receta.html', {'form': form, 'receta': receta})

def realizar_actualizacion_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        form = RecetaForm(request.POST, instance=receta)
        if form.is_valid():
            form.save()
            return redirect('ver_recetas')
    else:
        form = RecetaForm(instance=receta)
    return render(request, 'receta/actualizar_receta.html', {'form': form, 'receta': receta})

@csrf_protect
def borrar_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    if request.method == 'POST':
        receta.delete()
        return redirect('ver_recetas')
    return render(request, 'receta/borrar_receta.html', {'receta': receta})

# Vistas de Factura
def agregar_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ver_facturas')
    else:
        form = FacturaForm()
    return render(request, 'factura/agregar_factura.html', {'form': form})

def ver_facturas(request):
    facturas = Factura.objects.all()
    return render(request, 'factura/ver_facturas.html', {'facturas': facturas})

def actualizar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    form = FacturaForm(instance=factura)
    return render(request, 'factura/actualizar_factura.html', {'form': form, 'factura': factura})

def realizar_actualizacion_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        form = FacturaForm(request.POST, instance=factura)
        if form.is_valid():
            form.save()
            return redirect('ver_facturas')
    else:
        form = FacturaForm(instance=factura)
    return render(request, 'factura/actualizar_factura.html', {'form': form, 'factura': factura})

@csrf_protect
def borrar_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    if request.method == 'POST':
        factura.delete()
        return redirect('ver_facturas')
    return render(request, 'factura/borrar_factura.html', {'factura': factura})
