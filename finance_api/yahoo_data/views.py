from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from yahoo_data.models import HistoricalData
from yahoo_data.serializers import HistoricalDataSerializer


class HistoricalDataList(generics.ListAPIView):
    """List of all data for specific tickers"""
    serializer_class = HistoricalDataSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned queryset to a given ticker,
        by filtering against a `ticker` query parameter in the URL.
        """
        queryset = HistoricalData.objects.all()
        ticker = self.request.query_params.get("ticker")
        if ticker is not None:
            queryset = queryset.filter(ticker=ticker)
        return queryset
