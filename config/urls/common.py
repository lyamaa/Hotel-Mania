from rest_framework_extensions.routers import ExtendedDefaultRouter

from commons.api.views import ConfigChoiceCategoryViewsets, ConfigChoiceViewsets

router = ExtendedDefaultRouter()

urlpatterns = []


router.register(
    "config/choice/category", ConfigChoiceCategoryViewsets, basename="cc-category"
)
router.register("Config/choice", ConfigChoiceViewsets, basename="c-choice")


urlpatterns += router.urls
