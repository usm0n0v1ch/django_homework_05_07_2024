from typing import re

from django import forms
from django.core.exceptions import ValidationError

from validation_app.models import MyUser



class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = '__all__'

    # def clean_name(self):
    #     name = self.cleaned_data.get('name')
    #     if name and len(name) < 3:
    #         raise ValidationError('Имя должно содержать больше 3 символов')
    #     return name
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     if email and 'spam' in email.lower():
    #         raise ValidationError('Адрес электронной почты не должен содержать слово "spam"')
    #     return email
    #
    # def validate_strong_password(self, password):
    #
    #     if len(password) < 8:
    #         raise ValidationError('Пароль должен содержать не менее 8 символов')
    #     if not re.search(r'[A-Z]', password):
    #         raise ValidationError('Пароль должен содержать хотя бы одну заглавную букву')
    #     if not re.search(r'[a-z]', password):
    #         raise ValidationError('Пароль должен содержать хотя бы одну строчную букву')
    #     if not re.search(r'[0-9]', password):
    #         raise ValidationError('Пароль должен содержать хотя бы одну цифру')
    #     if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    #         raise ValidationError('Пароль должен содержать хотя бы один специальный символ')
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get("password")
    #     password_confirm = cleaned_data.get("password_confirm")
    #
    #     if password and password_confirm and password != password_confirm:
    #         raise ValidationError('Пароли не совпадают.')
    #
    #     if password:
    #         self.validate_strong_password(password)
    #
    #     return cleaned_data

