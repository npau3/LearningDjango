from .models import Task
from django.forms import ModelForm, TextInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["product", "amount"]
        widgets = {
            "product": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название'
            }),
            "amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество'
            }),

        }
