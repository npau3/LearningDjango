from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField('Название', max_length=50)
    amount = models.IntegerField('Количество')

    def __str__(self):
        return self.product
            # , self.product + '|' + str(self.author)

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
