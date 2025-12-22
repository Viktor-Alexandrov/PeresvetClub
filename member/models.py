from django.db import models

class Member(models.Model):
    """Модель спортсмена клуба"""

    first_name = models.CharField(max_length=20)  # имя
    patronymic = models.CharField(max_length=30)  # отчество
    last_name = models.CharField(max_length=50)   # фамилие
