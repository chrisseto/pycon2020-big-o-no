from django.db import models
from include import IncludeManager

class User(models.Model):
    name = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    col1 = models.TextField(default='col1')
    col2 = models.TextField(default='col2')
    col3 = models.TextField(default='col2')

    objects = IncludeManager()


class Email(models.Model):
    email = models.TextField()
    user = models.ForeignKey(User, related_name='emails', on_delete=models.CASCADE)

    objects = IncludeManager()


class Tag(models.Model):
    text = models.TextField()


class Project(models.Model):
    title = models.TextField()
    body = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    col1 = models.TextField(default='col1')
    col2 = models.TextField(default='col2')
    col3 = models.TextField(default='col2')
    tags = models.ManyToManyField(Tag)

    objects = IncludeManager()


class Contributor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, related_name='contributors', on_delete=models.CASCADE)
    col1 = models.TextField(default='col1')
    col2 = models.TextField(default='col2')
    col3 = models.TextField(default='col2')

    objects = IncludeManager()
