from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length = 120)
    content = models.TextField()

    def __str__(self):
        return self.title