from django.db import models
from django.db.models.deletion import CASCADE


class List(models.Model):
    """отдельный список"""
    pass


class Item(models.Model):
    """элемент списка"""
    text = models.TextField(default='')
    list = models.ForeignKey(List, on_delete=CASCADE, default=None)
