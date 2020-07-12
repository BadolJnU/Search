from django.db import models

# Create your models here.

class SearchHistory(models.Model):
    loginuser = models.CharField(max_length=300)
    keyword = models.CharField(max_length=300)
    searchdate = models.DateTimeField()
    searchresult = models.CharField(max_length=200)

    def __str__(self):
        return self.loginuser + ' searched this ' + self.keyword

