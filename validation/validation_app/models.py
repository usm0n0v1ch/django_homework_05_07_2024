from django.db import models
from django.core.exceptions import ValidationError
import re

class MyUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    password_confirm = models.CharField(max_length=200)

    def clean(self):
        super().clean()

        if self.name and len(self.name) < 3:
            raise ValidationError('Имя должно содержать больше 3 символов')

        if self.email and 'spam' in self.email.lower():
            raise ValidationError('Адрес электронной почты не должен содержать слово "spam"')


        self.validate_strong_password(self.password)
        if self.password != self.password_confirm:
            raise ValidationError('Пароли не совпадают')

    def validate_strong_password(self, password):
        if len(password) < 8:
            raise ValidationError('Пароль должен содержать не менее 8 символов')
        if not re.search(r'[A-Z]', password):
            raise ValidationError('Пароль должен содержать хотя бы одну заглавную букву')
        if not re.search(r'[a-z]', password):
            raise ValidationError('Пароль должен содержать хотя бы одну строчную букву')
        if not re.search(r'[0-9]', password):
            raise ValidationError('Пароль должен содержать хотя бы одну цифру')
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('Пароль должен содержать хотя бы один специальный символ')

    def save(self, *args, **kwargs):
        self.clean()
        super(MyUser, self).save(*args, **kwargs)
