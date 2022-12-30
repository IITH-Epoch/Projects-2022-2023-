from django.db import models
from os.path import join

ct=0
def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    global ct
    filename = "image_%d.%s" % (ct, ext)
    ct+=1
    fname=join('img', filename)
    return fname

class pic(models.Model):
    picture = models.FileField(upload_to=content_file_name)