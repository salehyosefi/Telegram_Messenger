from django.db import models
from datetime import datetime

class Detail(models.Model):
    name = models.CharField(max_length=40)
    lastMessage = models.CharField(max_length=50)
    unreadMessagesCount = models.IntegerField(blank=True)
    image = models.ImageField(default='user_image/default_profile.png', upload_to='user_image/', null=True, blank=True)
    date = models.DateTimeField(default=datetime.now)
    pin = models.BooleanField(default=False)
    mute = models.BooleanField(default=False)
    seen = models.BooleanField(default=False)
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.name
