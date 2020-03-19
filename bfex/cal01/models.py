from django.db import models

# brew model
class Brew(models.Model):
    name = models.CharField(max_length=200)
    brew_date = models.DateTimeField('date published')

