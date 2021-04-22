from django.db import models

# Create your models here.
class DeviceStats(models.Model):
	device_id = models.CharField(max_length=100)
	device_type = models.CharField(max_length=100, default="")

	cpu_usage = models.IntegerField()
	mem_usage = models.IntegerField()
