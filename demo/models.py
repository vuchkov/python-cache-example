# coding: utf-8
from django.db import models


class Foo(models.Model):
    name = models.CharField(max_length=50)
    pre_serialized = models.JSONField(blank=True, null=True)


class Bar(models.Model):
    foo = models.ForeignKey(Foo, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)


class Baz(models.Model):
    name = models.CharField(max_length=50)


class Zab(models.Model):
    bar = models.ForeignKey(Bar, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    bazs = models.ManyToManyField(Baz)
