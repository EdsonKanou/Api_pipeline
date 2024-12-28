from mon_api.models import Sensor
from rest_framework import serializers

class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = [
            'id', 
            'GENDER', 
            'AGE', 
            'SMOKING', 
            'YELLOW_FINGERS', 
            'ANXIETY', 
            'PEER_PRESSURE', 
            'CHRONIC_DISEASE', 
            'FATIGUE', 
            'ALLERGY', 
            'WHEEZING', 
            'ALCOHOL_CONSUMING', 
            'COUGHING', 
            'SHORTNESS_OF_BREATH', 
            'SWALLOWING_DIFFICULTY', 
            'CHEST_PAIN', 
            'LUNG_CANCER'
        ]
