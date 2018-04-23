from .models import Entity, EntityRelationship
from rest_framework import serializers


class EntitySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Entity
        fields = ("account_number", "display_name", "ids", "tags", "facts")