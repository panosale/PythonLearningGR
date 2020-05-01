import time
from cv2 import putText as pt 
from cv2 import FONT_HERSHEY_PLAIN as fnt

class FPS: # To measure the number of frame per second
    def __init__(self):
        self.nbf=0
        self.fps=0
        self.start=0
        
    def update(self):
        if self.nbf%10==0:
            if self.start != 0:
                self.stop=time.time()
                self.fps=10/(self.stop-self.start)
                self.start=self.stop
            else :
                self.start=time.time()    
        self.nbf+=1
    
    def get(self):
        return self.fps

    def display(self, win, orig=(10,30), font=fnt, size=2, color=(0,255,0), thickness=2):
        pt(win,f"FPS={self.get():.2f}",orig,font,size,color,thickness)
