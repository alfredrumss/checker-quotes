from rest_framework import routers

from core.views import QuoteViewSet

router = routers.SimpleRouter()
router.register(r"", QuoteViewSet, basename="quotes")
urlpatterns = router.urls
