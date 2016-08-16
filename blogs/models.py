from __future__ import unicode_literals

from django.db import models
import datetime
from django_extensions.db import fields
from django.utils import timezone

class Article(models.Model):
    CATEGORIES = (
        ('List','List'),
        ('Blog','Blog'),
        ('Countdown','Countdown'),
        )

    title = models.CharField(max_length=200)
    text = models.TextField()
    description = models.CharField(max_length=500)
    pic = models.URLField(max_length=200)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length = 200)
    author_pic = models.URLField(max_length=200)
    slug = fields.AutoSlugField(populate_from = 'title')
    category = models.CharField(choices = CATEGORIES, max_length=250) 
    is_approved = models.BooleanField(default = False)

    def __str__(self):
        return self.text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() -datetime.timedelta(days =1)



class ListItem(models.Model):
    item = models.ForeignKey(Article, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pic = models.URLField(max_length=200, null=True, blank=True)


class CountdownItem(models.Model):
    countdown = models.ForeignKey(Article, on_delete = models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    pic = models.URLField(max_length=200, null=True, blank=True)


