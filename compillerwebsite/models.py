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
    feature_Image = models.ImageField(default='feature_default.jpg', upload_to='feature_Images')
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


class Style(models.Model):
    home_Cover = models.ImageField(default='default_cover.jpg', upload_to='cover_Image', blank=True, null=True)
    team_Cover = models.ImageField(default='default_cover.jpg', upload_to='cover_Image', blank=True, null=True)
    research_Cover = models.ImageField(default='default_cover.jpg', upload_to='cover_Image', blank=True, null=True)
    publications_Cover = models.ImageField(default='default_cover.jpg', upload_to='cover_Image', blank=True, null=True)
    news_Cover = models.ImageField(default='default_cover.jpg', upload_to='cover_Image', blank=True, null=True)
    opportunity_Cover = models.ImageField(default='default_cover.jpg', upload_to='cover_Image', blank=True, null=True)
    home_slideshow_image_1 = models.ImageField(default='default_slide.jpg', upload_to='slide_Image', blank=True,
                                               null=True)
    home_slideshow_image_2 = models.ImageField(default='default_slide.jpg', upload_to='slide_Image', blank=True,
                                               null=True)
    home_slideshow_image_3 = models.ImageField(default='default_slide.jpg', upload_to='slide_Image', blank=True,
                                               null=True)
