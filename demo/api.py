# coding: utf-8
import json

from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.serializers import ModelSerializer, ListSerializer

from demo.models import Foo, Bar, Baz, Zab


class BazSerializer(ModelSerializer):
    class Meta:
        model = Baz
        fields = ("name", )


class ZabSerializer(ModelSerializer):
    bazs = BazSerializer(many=True)

    class Meta:
        model = Zab
        fields = ("name", "bazs")


class BarSerializer(ModelSerializer):
    zab_set = ZabSerializer(many=True)

    class Meta:
        model = Bar
        fields = ("name", "zab_set")


class FooSerializer(ModelSerializer):
    bar_set = BarSerializer(many=True)

    class Meta:
        model = Foo
        fields = ("name", "bar_set")

    def to_representation(self, instance):
        if instance.pre_serialized:
            return instance.pre_serialized
        return super().to_representation(instance)

    @property
    def data_skip_cache(self):
        return super().to_representation(self.instance)


class FooListView(ListAPIView):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer


class FooRetrieveView(RetrieveAPIView):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer
