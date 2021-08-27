from rest_framework import serializers
from main.models import Project

class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('headline', 'link', 'thumbnail', 'color')