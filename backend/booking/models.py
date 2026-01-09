from django.db import models

class MeetingType(models.Model):
    name = models.CharField(max_length=100) #název schůzky
    duration_actual = models.IntegerField() #Skutečná délka v minutách
    duration_with_buffer = models.IntegerField() #Délka + přestávka
    meeting_kind = models.CherField(
        max_length=10,
        choices=[("online", "Online"), ("in_person", "Osobní") ]
    )

class Booking(models.Model):
    meeting_type = models.ForeignKey(MeetingType, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=20, default='confirmed')
    google_meet_link = models.URLField(blank=True, null=True)

    def __str__(self):          #pouze pro test v adminu
        return f"{self.meeting_type.name} at {self.start_time}"
    