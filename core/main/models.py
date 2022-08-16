from django.db import models

# Create your models here.
class Fibonacci(models.Model):
    name = models.CharField('Fibonacci name', max_length=30)
    about = models.TextField('Fibonacci about')
    img = models.ImageField('Fibonacci image', upload_to='media')

    def __str__(self):
        return self.name