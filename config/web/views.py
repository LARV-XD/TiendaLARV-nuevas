from django.shortcuts import render

from web.formularios.formularioPlatos import FormularioRegistroPlatos
from web.formularios.formularioEmpleados import FormularioRegistroEmpleados
from web.models import Platos,Empleados
# Create your views here.

#CADA VISTA ES UNA FUNCION DE PY

def Home(request):
    return render(request,'index.html')

def PlatosVista(request):

    #cargar el formulario de registro de platos
    formulario=FormularioRegistroPlatos()

    #Creamos un diccionario para enviar datos hacia el template
    diccionarioEnvioDatos={
        'formulario':formulario
    }
    
    #Recibiendo datos del formulario
    #PETICION DE TIPO POST
    if request.method=='POST':
        datosFormulario=FormularioRegistroPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            #ENVIAR DATOS A MI DB
            platoNuevo = Platos(
                nombre= datosLimpios["nombrePlato"],
                descripcion = datosLimpios["descripcionPlato"],
                imagen= datosLimpios["fotoPlato"],
                precio= datosLimpios["precioPlato"],
                tipo= datosLimpios["tipoPlato"]
            )
            platoNuevo.save()   

    return render(request,'platos.html',diccionarioEnvioDatos)


def EmpleadosVista(request):
    formulario = FormularioRegistroEmpleados()

    envioDatos={
        'formEmpleados':formulario
    }

    if(request.method == 'POST'):
        datosFormulario = FormularioRegistroEmpleados(request.POST)
        if(datosFormulario.is_valid()):
            datoslimpios= datosFormulario.cleaned_data
            print(datoslimpios)
            #ENVIAR DATOS A MI DB EMPLEADOS
            empleadoNuevo = Empleados(
                nombre=datoslimpios["nombreEmpleado"],
                apellido=datoslimpios["ApellidoEmpleado"],
                edad=datoslimpios["EdadEmpleado"],
                telefono=datosFormulario["TelefonoEmpleado"],
                salario=datoslimpios["SaldoEmpleado"]
            )
            empleadoNuevo.save()
    return render(request, 'empleados.html',envioDatos)