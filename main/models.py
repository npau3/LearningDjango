from django.db import models


class Task(models.Model):
    product = models.CharField('Название', max_length=50)
    amount = models.IntegerField('Количество')

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
