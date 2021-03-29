from rest_framework import serializers
from .models import NodeTypes, NodesHierarchy


class NodeTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = NodeTypes
        fields = '__all__'
        read_only_fields = ('id', 'description')

class NodesHierarchySerializer(serializers.ModelSerializer):
    full_type = serializers.ReadOnlyField(source="NodeTypes.description")

    class Meta:
        model = NodesHierarchy
        fields = '__all__'
        read_only_fields = ('id',)
