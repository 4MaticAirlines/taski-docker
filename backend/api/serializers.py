"""TaskSerializer."""
from rest_framework import serializers

from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    """TaskSerializer."""

    class Meta:
        """TaskSerializer."""

        model = Task
        fields = ('id', 'title', 'description', 'completed')
