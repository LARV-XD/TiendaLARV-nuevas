from django import forms

class FormularioRegistroEmpleados(forms.Form):
    nombreEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="nombre"
    )
    ApellidoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Apellido"
    )
    EdadEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Edad"
    )
    TelefonoEmpleado=forms.CharField(
        widget=forms.TextInput(attrs={"class":"form-control mb-3"}),
        max_length=25,
        required=True,
        label="Telefono"
    )
    SaldoEmpleado=forms.CharField(
        widget=forms.NumberInput(attrs={"class":"form-control mb-3"}),
        max_length=8,
        required=True,
        label="Salario"
    )
    
