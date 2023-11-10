from django.db import models

# Create your models here.
class Drawing(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField(default='')
    imgfile = models.ImageField(null=True, upload_to="", blank=True)
    uploadedFile = models.FileField(upload_to="result/")
    create_date = models.DateTimeField()
    
    def __str__(self):
        return self.subject

class Comment(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()