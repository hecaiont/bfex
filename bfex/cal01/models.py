from django.db import models

# brew model
class Brew(models.Model):
    
    brew_name = models.CharField(max_length=100)
    brew_date = models.DateTimeField('date published')
    brew_description = models.CharField(max_length=200)
    
    # def ingredients
    total_water = 
    total_rice = 
    total_stage = 
    total_additive = 

    def __str__(self):
        return self.name



class stage(models.Model):


    stage_order = 
    stage_type = 
    stage_description = 
    stage_date = 
    
    
    # def ingredients    
    rice = 
    water = 
    yeast = 
    additive = 
