from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=1000)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class NewsArticle(models.Model):
    title = models.CharField(max_length=1000)
    date = models.DateField(auto_now=False, auto_now_add=False, null=True)
    summary = models.CharField(max_length=1000)
    body = models.TextField()
    link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title


class Assignment(models.Model):
    title = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    description = models.TextField()
    requirements = models.CharField(max_length=1000, blank=True)
    deadline = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title