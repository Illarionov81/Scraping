from django.shortcuts import get_object_or_404
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from api_v1.serializers import CompanySerializer
from webapp.models import Company


class CompanyViewSet(ViewSet):
    queryset = Company.objects.all()

    def list(self, request):
        objects = Company.objects.all()
        slr = CompanySerializer(objects, many=True, context={'request': request})
        return Response(slr.data)

    def retrieve(self, request, pk=None):
        article = get_object_or_404(Company, pk=pk)
        slr = CompanySerializer(article, context={'request': request})
        return Response(slr.data)

