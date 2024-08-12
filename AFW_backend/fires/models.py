from django.db import models

class WildfireReport(models.Model):
    date = models.DateField()
    summary = models.TextField()
    details = models.TextField()

    def __str__(self):
        return f"Wildfire Report - {self.date}"


# class WildfireDetail(models.Model):
#     wildfire = models.ForeignKey(Wildfire, related_name='details', on_delete=models.CASCADE)
#     detail_text = models.TextField()
