# -*- coding: utf-8 -*-

from django.db import models


class Student(models.Model):

    class Meta:
        db_table = 'students'
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    name = models.CharField(verbose_name='Имя', max_length=50)  # Имя
    surname = models.CharField(verbose_name='Фамилия', max_length=50)  # Фамилия
    father_name = models.CharField(verbose_name='Отчество', blank=True, max_length=50)  # Отчество
    date_of_birth = models.DateField(verbose_name='День рождения', default=0)  # День рождения
    student_card = models.CharField(verbose_name='Студенческий билет', max_length=50)  # Студенческий билет
    group = models.ForeignKey('group.Group', null=True, blank=True, verbose_name='Группа студента')  # Группа студента

    def get_name(self):
        return "%s %s %s" % (self.surname, self.name, self.father_name)

    def __str__(self):
        return u"{0} {1} {2}".format(self.surname, self.name, self.father_name, )