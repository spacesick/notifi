from rest_framework import serializers

from .models import Listing


class ListingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Listing
        fields = [
            'url',
            'name',
            'crawl_url',
            'selector',
            'period',
            'is_active',
            'user',
            'content_hash',
            'date_created',
        ]
        lookup_field = 'url'
