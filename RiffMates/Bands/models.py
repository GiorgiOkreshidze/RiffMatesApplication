from django.db import models

# Create your models here.
class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth = models.DateField()

    def __str__(self):
        return f"Musician(id = {self.id}, last_name = {self.last_name})"
    
class Venue(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        ordering = ["name"]
    
    def __str__(self):
        return f"Venue(id = {self.id}, name = {self.name})"
        
    
class Room(models.Model):
    name  = models.CharField(max_length=20)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Room(id = {self.id}, name = {self.name})"

class Band(models.Model):
    name = models.CharField(max_length=20)
    musicians = models.ManyToManyField(Musician)
    
    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"Band(id = {self.id}, name = {self.name})"