from django import forms
from projectDjangoApp.models import Proyecto

class FromProyecto(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'