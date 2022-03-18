from django.forms import ModelForm, fields
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'email', 'username', 'password1', 'password2', 'car_number']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        # self.fields['title'].widget.attrs.update({'class':'input', 'placeholder':'Add title'})

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
