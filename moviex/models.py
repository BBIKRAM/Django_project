from django.db import models

# Create your models here.
class gener(models.Model):
    name = models.CharField(max_length=22)
    
    def __str__(self):
        return self.name

class movies(models.Model):
    title = models.CharField(max_length=233)
    cost = models.IntegerField()
    # something = models.IntegerField()

    def __str__(self):
        return self.title