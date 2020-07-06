from django.db import models

# Create your models here.

class Post(models.Model):
    no = models.AutoField(primary_key="True")
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(blank="True")
    slug = models.CharField(max_length=200)

    def __str__(self):
        return self.title + 'by' + self.author
