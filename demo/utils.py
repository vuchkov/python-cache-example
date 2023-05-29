# coding: utf-8
from django.db import transaction

from demo.models import Foo, Bar, Zab, Baz
from demo.api import FooSerializer


def random_data():
    for f in range(1, 4):
        with transaction.atomic():
            foo = Foo.objects.create(name=f)

            for b in range(1, 1000):
                bar = Bar.objects.create(foo=foo, name=b)

                for z in range(1, 30):
                    zab = Zab.objects.create(bar=bar, name=z)

                    for bz in range(1, 9):
                        baz = Baz.objects.create(name=bz)
                        zab.bazs.add(baz)


def pre_serialize():
    for foo in Foo.objects.all():
        serializer = FooSerializer(instance=foo)
        foo.pre_serialized = serializer.data_skip_cache
        foo.save()
