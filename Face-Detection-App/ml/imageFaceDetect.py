def image_face_detector(path):
    """
    ==========================
    For face detection
    ==========================
    """
    from os.path import join
    from cv2 import imread, imwrite, resize
    from mediapipe import solutions
    from faceDetect.settings import MEDIA_ROOT
    from ml.faceDetecModule import FaceDetector
    resize_bool = False
    ext = path.split('.')[-1]
    name=(path.split('/')[-1]).split('.')[0]
    detector=FaceDetector(minDetecCon=0.35)
    img = imread(path)
    h,w,c = img.shape
    if (h>1280 and w>720):
        img = resize(img,(1280,720))
        resize_bool = True
    img,li=detector.findFaces(img)
    imwrite(join(MEDIA_ROOT,f'img/{name}_result.{ext}'),img)
    return (resize_bool,len(li))
