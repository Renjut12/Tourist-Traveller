from django.db import models

# Create your models here.


class mytable(models.Model):
    name = models.CharField(max_length=200)
    picture = models.ImageField(upload_to='Table_image')
    descriptions = models.TextField()

    def __str__(self):
        return self.name
