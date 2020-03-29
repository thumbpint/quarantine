from django.db import models
from django.contrib.auth.models import User

class Shelter(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    builder = models.ForeignKey(User, on_delete=models.CASCADE)


    def pretty_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:50]