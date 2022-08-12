from django.db import models
from django.utils import timezone


class Chat(models.Model):
    chat_id = models.IntegerField
    created_at = models.DateTimeField(
        'Когда парсился чат',
        default=timezone.now,
        db_index=True
    )
    updated_at = models.DateTimeField(
        'Когда обновлялся',
        default=timezone.now(),
    )

    def __str__(self):
        return self.chat_id


class HR(models.Model):
    tg_id = models.IntegerField(
        'Tg ID',
        max_length=200
    )
    created_at = models.DateTimeField(
        'Когда парсился в первый раз',
        default=timezone.now,
        db_index=True
    )
    updated_at = models.DateTimeField(
        'Дата обновления',
        default=timezone.now(),
    )

    chat = models.ManyToManyField(
        Chat,
        verbose_name='В каких чатах состоит',
        related_name='hrs',
        blank=True
    )

    def __str__(self):
        return self.tg_id



