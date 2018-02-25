from django.db import models
from django.db.models.signals import pre_save, post_delete
from django.dispatch import receiver
from students.models import Student
from group.models import Group


class Logger(models.Model):

    class Meta:
        db_table = 'logger'
        verbose_name = 'Logger'
        verbose_name_plural = 'Loggers'

    CREATE = '1'
    MODIFIED = '2'
    DELETED = '3'

    TYPES = (
        (CREATE, 'Создано'),
        (MODIFIED, 'Модифицировано'),
        (DELETED, 'Удалено')
    )

    type = models.CharField(
        verbose_name='Используемое топливо',
        max_length=20,
        choices=TYPES,
        default=CREATE) # Тип
    date = models.DateTimeField('Date', auto_now=True)  # Дата
    model = models.CharField('Class', max_length=250)  # Модель
    log = models.CharField('Log', max_length=250)

    def __unicode__(self):
        return "%s: %s" % (self.date.strftime("%d.%m.%Y %H:%M"), self.log)


@receiver(pre_save, sender=Student)
@receiver(pre_save, sender=Group)
def model_save_signal(sender, instance, signal, *args, **kwargs):
    item = Logger()
    item.model = str(sender)
    try:
        sender.objects.get(pk=instance.pk)
        item.type = 'MODIFIED'
        item.log = 'Модифицировано'
    except sender.DoesNotExist:
        item.type = 'CREATE'
        item.log = 'Создано'
    item.log = 'Object <%s> ' % instance + item.log
    item.save()


@receiver(post_delete, sender=Student)
@receiver(post_delete, sender=Group)
def model_delete_signal(sender, instance, signal, *args, **kwargs):
    item = Logger()
    item.model = str(sender)
    item.type = 'DELETED'
    item.log = 'Обьект <%s> удален' % instance
    item.save()