from rest_framework import serializers
from main.models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):

    thumbnail = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Project
        fields = ('headline', 'link', 'thumbnail', 'color')

    def get_image_url(self, obj):
        request = self.context.get('request')
        image_url = obj.thumbnail.url
        return request.build_absolute_uri(image_url)