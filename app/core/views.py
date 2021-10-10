from rest_framework import mixins, viewsets, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from core.models import Quote
from core.serializers import QuoteSerializer
from .utils import fetch_quotes


class QuoteViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
    # permission_classes = [AllowAny]
    permission_classes = [HasAPIKey]

    def create(self, request, *args, **kwargs):

        quote = fetch_quotes()
        # headers = self.get_success_headers(serializer.data)
        serializer = QuoteSerializer(quote)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
