from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Drawing(models.Model):
    subject = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_drawing')
    content = models.TextField(default='')
    imgfile = models.ImageField(null=True, upload_to="")
    uploadedFile = models.FileField(upload_to="result/")
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_drawing')

    def __str__(self):
        return self.subject

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_comment')

class Document(models.Model):
    uploadedFile = models.FileField(upload_to="result/", null=True, blank=True)
    dateTimeOfUpload = models.DateTimeField(auto_now=True)