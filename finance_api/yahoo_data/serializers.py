from rest_framework import serializers

from yahoo_data.models import HistoricalData


class HistoricalDataSerializer(serializers.ModelSerializer):
    """list Actors and Directors"""

    class Meta:
        model = HistoricalData
        fields = "__all__"
