from rest_framework.serializers import *

from apps.app.models import POst

class POstSerializer(ModelSerializer):
    
    class Meta:

        model = POst
        fields = '__all__'
        