from .models import Medcard
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput, NumberInput,Textarea, RadioSelect

CHOICES= [
    ('первичный', 'Первичный'),
    ('повторный', 'Повторный')
    ]

class MedcardForm(ModelForm):
    class Meta:
        model = Medcard
        fields = ['iin','lastname', 'firstname', 'surname', 'birthdate','faculty','group','status','diagnosis','suggestions','perv_povt','additions', 'address', 'simptoms']

        widgets = {
            "iin":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "lastname":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "firstname":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "surname":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "birthdate":NumberInput(attrs={
            'class': 'shadow form-control',
            'type': 'date'
            }),
            "faculty":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "group":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "status":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "address":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "simptoms":Textarea(attrs={
            'class': 'shadow form-control'
            }),
            "diagnosis":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "suggestions":TextInput(attrs={
            'class': 'shadow form-control'
            }),
            "perv_povt":RadioSelect(attrs={
            'class': 'form'
            }, choices=CHOICES),
            "additions":TextInput(attrs={
            'class': 'shadow form-control'
            }),
        }