from django.db import models


class Book(models.Model):
    name = models.CharField('書名', max_length=20)
    price = models.PositiveIntegerField('價格')
    introduction = models.TextField('簡介')

    def __str__(self):
        return '{} ({})'.format(self.name, self.id)
