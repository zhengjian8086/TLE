from rest_framework import viewsets

from .models import NodeTypes, NodesHierarchy
from .serializers import NodeTypesSerializer, NodesHierarchySerializer


class NodeViewSet(viewsets.ModelViewSet):
    queryset = NodesHierarchy.objects.all()
    serializer_class = NodesHierarchySerializer
