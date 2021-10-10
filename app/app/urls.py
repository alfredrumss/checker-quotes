from django.urls import include, path

API_PREFIX = "api/v1"

urlpatterns = [
    path(
        f"{API_PREFIX}/quotes",
        include(("core.urls", "core")),
    ),
]
