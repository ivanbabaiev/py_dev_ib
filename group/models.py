# -*- coding: utf-8 -*-

from django.db import models


class Group(models.Model):

    class Meta:
        db_table = 'group'
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

    name = models.CharField(verbose_name='Название группы', max_length=50)  # Название группы
    captain = models.ForeignKey('students.Student',
                                on_delete=models.SET_NULL,
                                verbose_name='Староста группы',
                                related_name="groups",
                                null=True,
                                blank=True)  # Староста группы

    def __str__(self):
        return u"{0}".format(self.name)

