from django.db import models

class Status(models.TextChoices):
    UNSTARTED = 'u', "Ещё не начата"
    ONGOING = 'o', "В процессе"
    FINISHED = 'f', "Закончена"


class Task(models.Model):
    name = models.CharField(verbose_name="Имя задачи", max_length=65, unique=True)
    status = models.CharField(verbose_name="Статус задачи", max_length=1, choices=Status.choices)

    def __str__(self):
        return self.name
