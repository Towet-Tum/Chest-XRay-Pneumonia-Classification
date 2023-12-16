from django.forms import ModelForm
from chest.models import  Diagnosis
from django.contrib.auth.models import User

class UserFormModel(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
