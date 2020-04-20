from django.db import models

# brew model
class Brew(models.Model):
    
    brew_name = models.CharField(primary_key=True ,max_length=100)
    brew_date = models.DateTimeField(auto_now_add=True)
    brew_description = models.TextField(verbose_name='내용')
    
    def doBrew(self, total_water, total_rice, total_stage):
        self.total_water = total_water
        self.total_rice = total_rice
        self.total_stage = total_stage
        # self.total_additive = total_additive
        self.RCMN_yeast = int(total_rice)*0.1

        # for i in range(int(self.total_stage)):
        #     eval('stg'+str(i)+' = stage()')


class stage(models.Model):
    stage_date = models.DateTimeField(auto_now_add=True)

    stage_order = models.IntegerField(max_length=10)
    stage_type = models.CharField(max_length=100)

    water = models.FloatField(null=True)
    rice = models.FloatField(null=True)
    yeast = models.FloatField(null=True)
    additive = models.FloatField(null=True)
    description = models.TextField(verbose_name='내용')

    def doStage(self, stage_order, stage_type, water, rice, yeast, additive, description):
        self.rice = water
        self.water = rice
        self.yeast = yeast
        self.additive = additive
        self.description = description


# class water(models.Model):
#     water_name = models.CharField(max_length=100)
#     water_amount = models.FloatField(null=True)
#     water_description = models.TextField(verbose_name='내용')

# class rice(models.Model):
#     rice_name = models.CharField(max_length=100)
#     rice_amount = models.FloatField(null=True)
#     rice_description = models.TextField(verbose_name='내용')

# class yeast(models.Model):
#     yeast_name = models.CharField(max_length=100)
#     yeast_amount = models.FloatField(null=True)
#     yeast_description = models.TextField(verbose_name='내용')

# class additive(models.Model):
#     additive_name = models.CharField(max_length=100)
#     additive_amount = models.FloatField(null=True)
#     additive_description = models.TextField(verbose_name='내용')
