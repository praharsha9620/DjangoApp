from rest_framework import serializers

class RawDeviceSerializer(serializers.Serializer):
    device_id = serializers.CharField(required=True, max_length=100)
    device_type = serializers.CharField(required=False, max_length=100)

    cpu_usage = serializers.IntegerField(required=False, min_value=0, default=0)
    mem_usage = serializers.IntegerField(required=False, min_value=0, default=0)
