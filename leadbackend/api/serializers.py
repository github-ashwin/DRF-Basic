from .models import *
from rest_framework import serializers

class LeadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lead
        fields = "__all__"
        read_only_fields = ['id','created_date','updated_at']