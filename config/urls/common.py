from rest_framework_extensions.routers import ExtendedDefaultRouter

from commons.api.views import (
    ConfigChoiceCategoryViewsets,
    ConfigChoiceViewsets,
    AddressViewsets,
    CompanyViewSets,
    CertificationTypeViewsets,
)

router = ExtendedDefaultRouter()

urlpatterns = []


router.register(
    "config/choice/category", ConfigChoiceCategoryViewsets, basename="cc-category"
)
router.register("config/choice", ConfigChoiceViewsets, basename="c-choice")
router.register("address", AddressViewsets, basename="c-address")
router.register("company", CompanyViewSets, basename="c-company")
router.register("certification", CertificationTypeViewsets, basename="c-certificate")


urlpatterns += router.urls
