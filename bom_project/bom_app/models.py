from django.db import models

class SiteInformation(models.Model):
    RAILWAY_LINE_CHOICES = [
        ('Midland', 'Midland'),
        ('FAL', 'FAL'),
        ('Fremantle', 'Fremantle'),
        ('Joondalup', 'Joondalup'),
        ('Ellenbrook', 'Ellenbrook'),
        ('Thornlie', 'Thornlie'),
        ('City Precinct', 'City Precinct'),
        ('Mandurah', 'Mandurah'),
    ]
    railway_line = models.CharField(max_length=100, choices=RAILWAY_LINE_CHOICES)
    ring_number = models.IntegerField()
    hostname = models.CharField(max_length=100, unique=True)
    btn_router_type = models.CharField(max_length=100, choices=[('7705-SAR-8', '7705-SAR-8'), ('7705-SAR-HC', '7705-SAR-HC')])
    site_type = models.CharField(max_length=100)

class Results(models.Model):
    site_information = models.ForeignKey(SiteInformation, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add other fields as needed

    def __str__(self):
        return f"Results for {self.site_information} at {self.timestamp}"
