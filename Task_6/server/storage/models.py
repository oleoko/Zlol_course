from django.db import models

# Create your models here.
class Key(models.Model):
	key_text = models.CharField(max_length = 200)
	key_ip = models.CharField(max_length = 20)
	def __str__(self):
		return self.key_text


