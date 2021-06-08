from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from commons.models import (
    Address,
    CertificationType,
    Company,
    ConfigChoice,
    ConfigChoiceCategory,
)
from rest_framework import serializers


class ConfigChoiceCategorySerializer(serializers.ModelSerializer):
    entered_by = serializers.StringRelatedField()

    class Meta:
        model = ConfigChoiceCategory

        fields = ("id", "name", "slug", "entered_by", "is_active")
        extra_kwargs = {"slug": {"read_only": True}}


class ConfigChoiceSerializer(serializers.ModelSerializer):

    entered_by = serializers.StringRelatedField()

    class Meta:
        model = ConfigChoice
        fields = (
            "id",
            "name",
            "description",
            "slug",
            "config_choice_category",
            "entered_by",
        )


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = (
            "id",
            "street_1",
            "street_2",
            "city",
            "state",
            "zip_code",
            "country",
            "location",
        )

        extra_kwargs = {"location": {"read_only": True}}


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "code",
            "description",
            "company_identification_number",
            "address",
            "logo",
        )


class CertificationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CertificationType
        fields = ("id", "certification_name", "system_name", "company")
