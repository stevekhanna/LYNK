from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=100)
    level = models.CharField(max_length=1000)
    phone = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=1000, blank=True)
    bio = models.TextField()

    def __str__(self):
        return self.name


class Feedback(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    comment = models.TextField(max_length=1000)

    def __str__(self):
        return self.student.name


class Assignment(models.Model):
    title = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    description = models.TextField()
    requirements = models.CharField(max_length=1000, blank=True)
    deadline = models.DateField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __str__(self):
        return self.title


class Grade(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    ASSIGNMENT_GRADES = (
        ('a+', "A+"), ('a', "A"), ('a-', "A-"),
        ('b+', "B+"), ('b', "B"), ('b-', "B-"),
        ('c+', "C+"), ('c', "C"), ('c-', "C-"),
        ('d+', "D+"), ('d', "D"), ('d-', "D-"),
        ('f', "F")
    )

    points = models.FloatField()
    letter_grade = models.CharField(choices=ASSIGNMENT_GRADES, max_length=3, default="A+")

    def __str__(self):
        return self.letter_grade
