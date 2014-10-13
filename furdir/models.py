from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.db.models.signals import post_save

class UserProfile(models.Model):  
    user = models.OneToOneField(User)
    species = models.CharField(max_length=30)
    birth_date = models.DateField()
    age = models.IntegerField()
    icon = models.ImageField(upload_to=('users/icons/%Y'), default="/static/images/default_icon.png")

    def calculate_age(self, bdate):
        today = date.today()
        age = today.year - bdate.year - ((today.month, today.day) < (bdate.month, bdate.day))
        return age

    def save(self, *args, **kwargs):
        self.age = self.calculate_age(self.birth_date)
        super(UserProfile, self).save(*args, **kwargs)

    def __unicode__(self):  
          return "%s's profile" % self.user  
