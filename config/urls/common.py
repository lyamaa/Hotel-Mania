from rest_framework_extensions.routers import ExtendedDefaultRouter

from commons.api.views import (
    ConfigChoiceCategoryViewsets,
    ConfigChoiceViewsets,
    AddressViewsets,
)

router = ExtendedDefaultRouter()

urlpatterns = []


router.register(
    "config/choice/category", ConfigChoiceCategoryViewsets, basename="cc-category"
)
router.register("config/choice", ConfigChoiceViewsets, basename="c-choice")
router.register("config/address", AddressViewsets, basename="c-address")


urlpatterns += router.urls
