from django.core.validators import URLValidator
from django.db import models

# Create your models here.
class Video(models.Model):
	id = models.CharField(max_length=50, primary_key=True, unique=True)
	embedded = models.CharField(max_length=255, validators=[URLValidator()])
	url = models.CharField(max_length=255, validators=[URLValidator()])
	rating = models.FloatField(default=0.0)
	channel = models.CharField(max_length=128)
	title = models.CharField(max_length=128)
	views = models.IntegerField(default=0)
	thumbnail = models.URLField()
	
	def __str__(self):
		return self.title

class Flipbook(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, default="")
	images = models.URLField()

	def __str__(self):
		return self.images

class Tag(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, default="")
	tags = models.CharField(max_length=255)

	def __str__(self):
		return self.tags

class Category(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, default="")
    categories = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.categories

class Actor(models.Model):
	video = models.ForeignKey(Video, on_delete=models.CASCADE, default="")
	actors = models.CharField(max_length=255, default="", blank=True)

	def __str__(self):
		return self.actors
