from rest_framework import serializers
from .models import Task
from datetime import datetime

class TaskSerializer(serializers.ModelSerializer):
    # Change to use both input and output formats
    due_date = serializers.DateTimeField(
        input_formats=["%Y-%m-%d %H:%M:%S", "iso-8601"],
        format="%Y-%m-%d %H:%M:%S",
        required=False,
        allow_null=True
    )
    completed_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('id', 'completed_date', 'created_at', 'updated_at')

    def validate_due_date(self, value):
        """Ensure due_date is in the future"""
        if value and value < datetime.now().astimezone(value.tzinfo):
            raise serializers.ValidationError("Due date must be in the future")
        return value