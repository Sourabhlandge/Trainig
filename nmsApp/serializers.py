from django.db.models import fields
from rest_framework import serializers
from .models import *

class ServerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServerInventory
        fields = "__all__"
