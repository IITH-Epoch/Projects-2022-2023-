from django.shortcuts import render,redirect
from django.http import HttpResponse
from os.path import join
import subprocess
from faceDetect.settings import MEDIA_ROOT,MEDIA_URL
from faceInImage.forms import picForm
from ml.imageFaceDetect import image_face_detector

accepted_files = ['jpg','jpeg','png','jpe']

# Main page
def main_view(request,*args, **kwargs):
    subprocess.call("rm -rf media/img/*", shell=True)
    """
    ==========================
    Main Page
    ==========================
    """
    context = {
        'extension':True,
        'MEDIA_URL':MEDIA_URL
    }
    if request.method=='POST':
        form = picForm(request.POST,request.FILES)
        if form.is_valid():
            pic = request.FILES['picture'].name
            ext = pic.split('.')[-1]
            global accepted_files
            if ext in accepted_files:
                fname=join('img', "image.%s" % (ext))
                result_img = join("img","image_result.%s" % (ext))
                form.save()
                resize,faces = image_face_detector(join(MEDIA_ROOT,fname))
                context['result_image']=result_img
                context['resize']=resize
                context['extension']=True
                context['faces']=faces
            else: context['extension']=False
    else:
        form = picForm()
    return render(request,'index.html',context)
