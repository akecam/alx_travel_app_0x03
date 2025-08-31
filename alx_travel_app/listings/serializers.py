from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Listing
        fields = "__all__"

    def validate_price_per_night(self, value):
        if value <= 0:
            serializers.ValidationError("price must be greater than 0")
        return value


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"
