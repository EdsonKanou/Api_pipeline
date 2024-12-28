from django.db import models

class Sensor(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]

    LUNG_CANCER_CHOICES = [
        ('YES', 'Yes'),
        ('NO', 'No'),
    ]

    GENDER = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=False)
    AGE = models.IntegerField(blank=False)
    SMOKING = models.IntegerField(blank=False)
    YELLOW_FINGERS = models.IntegerField(blank=False)
    ANXIETY = models.IntegerField(blank=False)
    PEER_PRESSURE = models.IntegerField(blank=False)
    CHRONIC_DISEASE = models.IntegerField(blank=False)
    FATIGUE = models.IntegerField(blank=False)
    ALLERGY = models.IntegerField(blank=False)
    WHEEZING = models.IntegerField(blank=False)
    ALCOHOL_CONSUMING = models.IntegerField(blank=False)
    COUGHING = models.IntegerField(blank=False)
    SHORTNESS_OF_BREATH = models.IntegerField(blank=False)
    SWALLOWING_DIFFICULTY = models.IntegerField(blank=False)
    CHEST_PAIN = models.IntegerField(blank=False)
    LUNG_CANCER = models.CharField(max_length=3, choices=LUNG_CANCER_CHOICES, blank=False)

    def __str__(self):
        return f"GENDER: {self.GENDER}, AGE: {self.AGE}, LUNG_CANCER: {self.LUNG_CANCER}"
