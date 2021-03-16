import datetime
from .models import NodesHierarchy
from haystack import indexes


class NodesHierarchyIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    name = indexes.CharField(model_attr='name')

    def get_model(self):
        return NodesHierarchy
 
    def index_queryset(self, using=None):
        return self.get_model().objects.all()
