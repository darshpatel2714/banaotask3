from django.db import models
from django.conf import settings
from datetime import datetime, timedelta

class Appointment(models.Model):
    patient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments_as_patient')
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments_as_doctor')
    speciality = models.CharField(max_length=100)
    appointment_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = (datetime.combine(datetime.today(), self.start_time) + timedelta(minutes=45)).time()
        super(Appointment, self).save(*args, **kwargs)

    def _str_(self):
        return f'Appointment with {self.doctor.get_full_name()} on {self.appointment_date} at {self.start_time}'