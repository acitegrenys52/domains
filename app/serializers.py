import requests
from requests.exceptions import ConnectionError
from rest_framework import serializers

from app.models import Domain


class DomainSerializer(serializers.ModelSerializer):
    def validate_url(self, url):
        protocol = url[0:5]

        if protocol != "https":
            raise serializers.ValidationError("Protocol is not https")

        try:
            r = requests.get(url)
            if r.status_code != 200:
                raise serializers.ValidationError("Response code is not 200")
        except ConnectionError as e:
            raise serializers.ValidationError("Connection error")

        return url

    class Meta:
        model = Domain
        fields = ('id', 'url')
