from django.db import models

# Create your models here.
class Language(models.Model):
    name = models.CharField(max_length=200,default="Not Specified")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'
    
class Catagory(models.Model):
    name = models.CharField(max_length=255,default="Not Speciifed")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.name}'
    

class Notes(models.Model):
    title = models.CharField(max_length=250,default="No title")
    language = models.ForeignKey(
        Language,related_name='language', on_delete=models.SET_NULL, blank=True, null=True)
    catagory = models.ForeignKey(
        Catagory,related_name='catagory', on_delete=models.SET_NULL, blank=True, null=True)
    note = models.TextField(default="You didn't add any note for this topic")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f'{self.title}'
    
    