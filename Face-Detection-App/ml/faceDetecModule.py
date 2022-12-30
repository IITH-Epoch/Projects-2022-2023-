from cv2 import cvtColor
from cv2 import rectangle
from cv2 import line
from cv2 import COLOR_BGR2RGB
from mediapipe import solutions

class FaceDetector:
    def __init__(self,minDetecCon=0.5,modelSel=False):
        self.minDetecCon=minDetecCon
        self.modelSel=modelSel
        self.mpFaceDet=solutions.face_detection
        self.mpDraw=solutions.drawing_utils
        self.faceDet=self.mpFaceDet.FaceDetection(self.minDetecCon,self.modelSel)
    def findFaces(self,img,draw=True):
        imgRGB=cvtColor(img,COLOR_BGR2RGB)
        self.results=self.faceDet.process(imgRGB)
        bboxs=[]
        if self.results.detections:
                for ids,detection in enumerate(self.results.detections):
                    bboxC=detection.location_data.relative_bounding_box
                    ih,iw,ic=img.shape
                    bbox=int(bboxC.xmin*iw),int(bboxC.ymin*ih),int(bboxC.width*iw),int(bboxC.height*ih)
                    if draw:
                        img = self.fancyDraw(img,bbox,l=20)
                        # cv2.putText(img,f'{int(detection.score[0]*100)}%',(bbox[0],bbox[1]-15),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2)
                    bboxs.append([ids,bbox,detection.score])
        return img,bboxs
    def fancyDraw(self,img,bbox,l=30,t=5,rt=1):
        x,y,w,h=bbox
        x1,y1=x+w,y+h
        rectangle(img,bbox,(255,0,255),rt)
        line(img,(x,y),(x+l,y),(255,0,255),t)
        line(img,(x,y),(x,y+l),(255,0,255),t)
        line(img,(x1,y),(x1-l,y),(255,0,255),t)
        line(img,(x1,y),(x1,y+l),(255,0,255),t)
        line(img,(x,y1),(x+l,y1),(255,0,255),t)
        line(img,(x,y1),(x,y1-l),(255,0,255),t)
        line(img,(x1,y1),(x1-l,y1),(255,0,255),t)
        line(img,(x1,y1),(x1,y1-l),(255,0,255),t)
        return img
# def main():
#     cap=cv2.VideoCapture(0)
#     ptime=0
#     ctime=0
#     detector=FaceDetector()
#     while True:
#         success, img=cap.read()
#         img,li=detector.findFaces(img)
#         if len(li):
#             print(li)
#         ctime=time.time()
#         fps=1/(ctime-ptime)
#         ptime=ctime
#         cv2.putText(img,f'FPS: {int(fps)}',(20,20),cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
#         cv2.imshow("Image",img)
#         cv2.waitKey(10)
#     cap.release()
#     cv2.destroyAllWindows()

# if __name__=='__main__':
#     main()