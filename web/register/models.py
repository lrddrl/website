from django.db import models

# Create your models here.

class article(models.Model):
    title = models.CharField('title', max_length = 200)
    img = models.FileField('pic', upload_to= 'media/img')
    content = models.TextField('content')
    c_time = models.DateTimeField('Date of create')