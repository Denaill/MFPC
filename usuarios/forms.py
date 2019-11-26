from .models import User
from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'address',
            'number',
            'city',
            'cc',
        ]
        labels = {
            'username' : 'Nombre de usuario',
            'first_name' : 'Nombre',
            'last_name' : 'Apellidos',
            'email' : 'Correo electronico',
            'address' : 'Direccion de residencia',
            'number' : 'Numero de contacto',
            'city' : 'Ciudad de residencia',
            'cc' : 'Cedula de ciudadania',
        }