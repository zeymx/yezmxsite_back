from rest_framework import serializers
from main.models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    thumbnail = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Project
        fields = ('headline', 'link', 'thumbnail', 'color')