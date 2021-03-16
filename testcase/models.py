from django.db import models

# Create your models here.
class NodesHierarchy(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    parent_id = models.PositiveIntegerField(blank=True, null=True)
    node_type_id = models.PositiveIntegerField()
    node_order = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'nodes_hierarchy'