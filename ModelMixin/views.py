from .models import ModelMixin
from .serializer import ModelMixinSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin


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


class ModelmixinRetrieve(GenericAPIView, RetrieveModelMixin):
    queryset = ModelMixin.objects.all()
    serializer_class = ModelMixinSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class ModelmixinUpdate(GenericAPIView, UpdateModelMixin):

    queryset = ModelMixin.objects.all()
    serializer_class = ModelMixinSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)



class ModelmixinDestroy(GenericAPIView, DestroyModelMixin):

    queryset = ModelMixin.objects.all()
    serializer_class = ModelMixinSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
