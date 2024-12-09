from django.db import models


class HomePgae(models.Model):
    video = models.FileField(upload_to='videos/')
    facebook = models.URLField(max_length=200, blank=True, null=True)
    instagram = models.URLField(max_length=200, blank=True, null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)
    youtube = models.URLField(max_length=200, blank=True, null=True)
    x = models.URLField(max_length=200, blank=True, null=True) 

    def __str__(self):
        return "HomePgae"