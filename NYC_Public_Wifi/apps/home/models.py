from django.db import models
from django.contrib.auth.models import User
import numpy as np

# Create your models here.


class Hotspot_Location(models.Model):
    obj_id = models.IntegerField(primary_key= True, unique = True, null= False)
    loc_name = models.CharField(max_length= 100, null= False)
    location = models.CharField(max_length= 100, null= False)
    latitude = models.FloatField(max_length= 100, null= True)
    longitude = models.FloatField(max_length= 100, null= True)
    X =  models.CharField(max_length= 100, null= True)
    Y =  models.CharField(max_length= 100, null= True)
    activated = models.CharField(max_length= 15, null= True)
    bin = models.IntegerField(null = True)
    bbl = models.IntegerField(null = True)

    def __str__(self):
        return str(self.obj_id) + " - " + self.location

    def average_rating(self):
        all_ratings = map(lambda x: x.rate, self.review_set.all())
        ar = np.mean(list(all_ratings)) # np -> numpy
        if (ar >=0 ):
            return ar
        else:
            return 0


#---------------------------#
#---- Provider Related -----#
#---------------------------#

   
class Provider(models.Model):
    prov_id = models.IntegerField(primary_key= True, unique = True, null= False)
    name = models.CharField(max_length= 70, null= False)
    ssid = models.CharField(max_length= 50, null= False)
    source_id = models.CharField(max_length= 50, null= True)
    type = models.CharField(max_length= 50, null= False)
    loc_type = models.CharField(max_length= 50, null= False)
    remarks = models.CharField(max_length= 100, null= True)

    def __str__(self):
        return str(self.prov_id) + " - " + self.name

class Hotspot_Provider(models.Model):
    obj_id = models.OneToOneField(Hotspot_Location, on_delete=models.CASCADE, null = False)
    prov_id = models.ForeignKey(Provider, on_delete=models.CASCADE, null = False)

    def __str__(self):
        return str(self.obj_id) + " - " + str(self.prov_id)


#---------------------------#
#----- Borough Related -----#
#---------------------------#


class Borough(models.Model):
    boro_code = models.SmallIntegerField(primary_key= True, unique = True, null= False)
    name = models.CharField(max_length= 70, null= False)

    def __str__(self):
        return str(self.boro_code) + " - " + self.name

class Hotspot_Borough(models.Model):
    obj_id = models.OneToOneField(Hotspot_Location, on_delete=models.CASCADE, null = False)
    boro_code = models.ForeignKey(Borough, on_delete=models.CASCADE, null = False)

    def __str__(self):
        return str(self.obj_id) + " - " + str(self.boro_code)

#---------------------------#
#--- Neighborhood Related --#
#---------------------------#


class Neighborhood(models.Model):
    ntacode =  models.CharField(max_length=5, primary_key= True, unique = True, null= False)
    postcode = models.SmallIntegerField( null= False)
    nta = models.CharField(max_length= 100, null= False)

    def __str__(self):
        return self.ntacode + " - " + self.nta

class Hotspot_Neighborhood(models.Model):
    obj_id = models.OneToOneField(Hotspot_Location, on_delete=models.CASCADE, null = False)
    ntacode = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, null = False)
    
    def __str__(self):
        return str(self.obj_id) + " - " + str(self.ntacode)





#---------------------------#
#----- Reviews Related -----#
#---------------------------#
class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    obj_id = models.ForeignKey(Hotspot_Location, on_delete=models.CASCADE, null = False)
    rate = models.IntegerField (choices = RATING_CHOICES, null=True)
    review = models.TextField(null = True)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    deleted = models.BooleanField(default=False)


class Modified_Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    old_review = models.ForeignKey(Review, on_delete=models.CASCADE)
    new_review = models.TextField(null = True)


# class Deleted_Review(models.Model):
#     owner = models.ForeignKey(User, on_delete=models.CASCADE)
#     review = models.ForeignKey(Review, on_delete=models.CASCADE)