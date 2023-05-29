from django.db import models

# Create your models here.
class Places(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    desc=models.TextField()

    def __str__(self):
        return self.name

class Team(models.Model):
    team_name=models.CharField(max_length=50)
    team_img=models.ImageField(upload_to='pics')
    team_desc=models.TextField()

    def __str__(self):
        return self.team_name