from django.db import models
from os.path import join

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "image.%s" % (ext)
    fname=join('img', filename)
    return fname

class pic(models.Model):
    picture = models.FileField(upload_to=content_file_name)
