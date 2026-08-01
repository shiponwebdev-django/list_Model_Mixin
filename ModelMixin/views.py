from .models import ModelMixin
from .serializer import ModelMixinSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin


class ModelMixinList(GenericAPIView, ListModelMixin):
    queryset = ModelMixin.objects.all()
    serializer_class = ModelMixinSerializer

    def get(self, request, *args, **kwargs):

        return self.list(request, *args, **kwargs)


class ModelMixinCreate(GenericAPIView, CreateModelMixin ):
    queryset = ModelMixin.objects.all()
    serializer_class = ModelMixinSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
