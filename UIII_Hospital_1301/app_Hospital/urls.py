from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio_hospital, name='inicio_hospital'),

    # URLs de Paciente
    path('pacientes/agregar/', views.agregar_paciente, name='agregar_paciente'),
    path('pacientes/ver/', views.ver_pacientes, name='ver_pacientes'),
    path('pacientes/actualizar/<int:paciente_id>/', views.actualizar_paciente, name='actualizar_paciente'),
    path('pacientes/actualizar/realizar/<int:paciente_id>/', views.realizar_actualizacion_paciente, name='realizar_actualizacion_paciente'),
    path('pacientes/borrar/<int:paciente_id>/', views.borrar_paciente, name='borrar_paciente'),

    # URLs de Doctor
    path('doctores/agregar/', views.agregar_doctor, name='agregar_doctor'),
    path('doctores/ver/', views.ver_doctores, name='ver_doctores'),
    path('doctores/actualizar/<int:doctor_id>/', views.actualizar_doctor, name='actualizar_doctor'),
    path('doctores/actualizar/realizar/<int:doctor_id>/', views.realizar_actualizacion_doctor, name='realizar_actualizacion_doctor'),
    path('doctores/borrar/<int:doctor_id>/', views.borrar_doctor, name='borrar_doctor'),

    # URLs de Cita
    path('citas/agregar/', views.agregar_cita, name='agregar_cita'),
    path('citas/ver/', views.ver_citas, name='ver_citas'),
    path('citas/actualizar/<int:cita_id>/', views.actualizar_cita, name='actualizar_cita'),
    path('citas/actualizar/realizar/<int:cita_id>/', views.realizar_actualizacion_cita, name='realizar_actualizacion_cita'),
    path('citas/borrar/<int:cita_id>/', views.borrar_cita, name='borrar_cita'),

    # URLs de Sala
    path('salas/agregar/', views.agregar_sala, name='agregar_sala'),
    path('salas/ver/', views.ver_salas, name='ver_salas'),
    path('salas/actualizar/<int:sala_id>/', views.actualizar_sala, name='actualizar_sala'),
    path('salas/actualizar/realizar/<int:sala_id>/', views.realizar_actualizacion_sala, name='realizar_actualizacion_sala'),
    path('salas/borrar/<int:sala_id>/', views.borrar_sala, name='borrar_sala'),

    # URLs de HistorialMedico
    path('historial/agregar/', views.agregar_historial, name='agregar_historial'),
    path('historial/ver/', views.ver_historiales, name='ver_historiales'),
    path('historial/actualizar/<int:historial_id>/', views.actualizar_historial, name='actualizar_historial'),
    path('historial/actualizar/realizar/<int:historial_id>/', views.realizar_actualizacion_historial, name='realizar_actualizacion_historial'),
    path('historial/borrar/<int:historial_id>/', views.borrar_historial, name='borrar_historial'),

    # URLs de Receta
    path('receta/agregar/', views.agregar_receta, name='agregar_receta'),
    path('receta/ver/', views.ver_recetas, name='ver_recetas'),
    path('receta/actualizar/<int:receta_id>/', views.actualizar_receta, name='actualizar_receta'),
    path('receta/actualizar/realizar/<int:receta_id>/', views.realizar_actualizacion_receta, name='realizar_actualizacion_receta'),
    path('receta/borrar/<int:receta_id>/', views.borrar_receta, name='borrar_receta'),

    # URLs de Factura
    path('factura/agregar/', views.agregar_factura, name='agregar_factura'),
    path('factura/ver/', views.ver_facturas, name='ver_facturas'),
    path('factura/actualizar/<int:factura_id>/', views.actualizar_factura, name='actualizar_factura'),
    path('factura/actualizar/realizar/<int:factura_id>/', views.realizar_actualizacion_factura, name='realizar_actualizacion_factura'),
    path('factura/borrar/<int:factura_id>/', views.borrar_factura, name='borrar_factura'),
]
