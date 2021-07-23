from .models import Task
from django.forms import ModelForm, TextInput, HiddenInput


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["product", "amount", "author"]
        widgets = {
            "product": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите название',
                'style': "width: 400px; height: 38px; margin-left: auto; margin-right: auto;",
                'maxlength': "10",
            }),
            "amount": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите количество',
                'style': "width: 400px; height: 38px; margin-left: auto; margin-right: auto;",
            }),
            "author": HiddenInput
        }
# style="width: 400px; height: 38px; margin-left: auto; margin-right: auto;"