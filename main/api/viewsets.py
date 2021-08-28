from main.models import Project
from .serializers import ProjectSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class ProjectViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Project.objects.all()
        serializer = ProjectSerializer(queryset, context={"request": request}, many=True)
        return Response(serializer.data)