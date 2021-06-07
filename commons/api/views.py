from commons.api.serializers import (
    ConfigChoiceCategorySerializer,
    ConfigChoiceSerializer,
)
from rest_framework import viewsets
from ..models import ConfigChoice, ConfigChoiceCategory


class ConfigChoiceCategoryViewsets(viewsets.ModelViewSet):
    queryset = ConfigChoiceCategory.objects.all()
    serializer_class = ConfigChoiceCategorySerializer

    def perform_create(self, serializer):
        serializer.save(entered_by=self.request.user)


class ConfigChoiceViewsets(viewsets.ModelViewSet):
    queryset = ConfigChoice.objects.all()
    serializer_class = ConfigChoiceSerializer

    def perform_create(self, serializer):
        serializer.save(entered_by=self.request.user)
