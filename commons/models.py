import random
import string

from autoslug import AutoSlugField
from core.models import CoreModel
from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from django.contrib.gis.db import models

User = get_user_model()


def slugify(value):
    return value.replace(" ", "-").lower()


class ConfigChoiceCategory(MPTTModel):
    """ """

    name = models.CharField(
        _("Config Choice Category Name"),
        help_text=_("Required and Unique"),
        max_length=255,
        unique=True,
    )
    slug = AutoSlugField(
        verbose_name=_("Config Choice Category Slug"),
        populate_from="name",
        slugify=slugify,
    )
    entered_by = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Config Choice Category")
        verbose_name_plural = _(" Config Choice Categories")

    def __str__(self):
        return self.name


class ConfigChoice(CoreModel):
    name = models.CharField(
        _("Config Choice Name"),
        help_text=_("Required and Unique"),
        max_length=255,
        unique=True,
    )
    description = models.TextField()
    slug = AutoSlugField(
        verbose_name=_("Config Choice Slug"),
        populate_from="name",
        slugify=slugify,
    )
    config_choice_category = models.ForeignKey(
        ConfigChoiceCategory, on_delete=models.CASCADE
    )
    entered_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Config Choice")
        verbose_name_plural = _("Config Choices")

    def __str__(self) -> str:
        return self.name


class Address(models.Model):
    street_1 = models.CharField(max_length=200)
    street_2 = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=100)
    country = models.CharField(max_length=50)
    location = models.PointField(null=True)

    def __str__(self):
        return f"{self.street_1}, {self.city}, {self.state}, {self.country}"


class Company(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=100)
    description = models.TextField()
    company_identification_number = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="logos", blank=True, null=True)

    def __str__(self):
        return self.name


class CertificationType(models.Model):
    certification_name = models.CharField(max_length=255)
    system_name = models.CharField(max_length=255, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    entered_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.certification_name
