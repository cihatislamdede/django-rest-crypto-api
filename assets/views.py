from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from assets.models import Asset
from assets.serializers import AssetSerializer


class AssetList(APIView):
    def get (self, request, format=None):
        assets = Asset.objects.all()
        serializer = AssetSerializer(assets, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class AssetDetail(APIView):
    def get(self, request, pk, format=None):
        snippet = get_object_or_404(Asset, pk=pk)
        serializer = AssetSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = get_object_or_404(Asset, pk=pk)
        serializer = AssetSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        snippet = get_object_or_404(Asset, pk=pk)
        snippet.delete()
        return Response(status=204)