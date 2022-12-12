# Third Party imports
from rest_framework import serializers

# Module imports
from .base import BaseSerializer

from plane.db.models import User, Module, ModuleMember


class ModuleWriteSerializer(BaseSerializer):

    members_list = serializers.ListField(
        child=serializers.PrimaryKeyRelatedField(queryset=User.objects.all()),
        write_only=True,
        required=False,
    )
    