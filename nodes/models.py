from django.db import models

# Create your models here.


class NodeTypes(models.Model):
    description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'node_types'


class NodesHierarchy(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    NodeTypes = models.ForeignKey(
        "NodeTypes", db_column="node_type_id", on_delete=models.DO_NOTHING, db_constraint=False)
    # node_type_id = models.PositiveIntegerField()
    node_order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes_hierarchy'
