import sys
from PyQt4 import QtGui, QtCore
#from functools import partial
import cv2
import matplotlib.pyplot as chang
import Cooretion 



class Window(QtGui.QMainWindow):
    def __init__(self):
        
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1600, 900)
        
        self.setWindowTitle("TEST CONTAMINATION FOR Prof.SUCHIN :)")
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))
      
        
        #--------------------------------TEXT BOX-----------------------------------------------
        '''
        self.text_br = QtGui.QLineEdit(self)
        self.text_br.resize(100,25)
        self.text_br.move(70,10)
        self.text_br.setText("1000000")

        self.text_port = QtGui.QLineEdit(self)
        self.text_port.resize(100,25)
        self.text_port.move(70,40)
        self.text_port.setText("COM15")
        '''
        self.home()   
        
    def home(self):
        
        newfont = QtGui.QFont("RSU", 20, QtGui.QFont.Bold) 

        l1 = QtGui.QLabel(self)
        l1.setText("Speckle Image")
        l1.setFont(newfont)
        l1.setGeometry(250,450,190,30)
        
        

        state = QtGui.QLabel(self)
        state.setText("state : ")
        state.setFont(newfont)
        state.setGeometry(800,730,200,20)
        #state.move(800,730)

        self.result = QtGui.QLabel(self)
        self.result.setText("-")
        self.result.setFont(newfont)
        self.result.setGeometry(890,750,500,20)
       
        self.status_txt = QtGui.QLabel(self)
        self.status_txt.setGeometry(800,50,500,500)
        movie = QtGui.QMovie("888.gif")
        self.status_txt.setMovie(movie)
   
        movie.start()
      


        '''

        l2 = QtGui.QLabel(self)
        l2.setText("Comport :")
        l2.move(10,40)

        pos_x = QtGui.QLabel(self)
        pos_x.setText("X :")
        pos_x.move(50,100)

        pos_y = QtGui.QLabel(self)
        pos_y.setText("Y :")
        pos_y.move(50,140)

        pos_z = QtGui.QLabel(self)
        pos_z.setText("Z :")
        pos_z.move(50,180)
        '''

        #-----------------------------IMAGE-----------------------------------
        '''
        self.pic = QtGui.QLabel(self) 
        self.pic.setGeometry(100, 50, 400, 400)
        pic1 =  cv2.imread("picture1.jpg")
        
        width = 400
        height =400
        dim = (width, height)
        pic1 = cv2.resize(pic1, dim, interpolation = cv2.INTER_AREA)
        image = QtGui.QImage(pic1, pic1.shape[1],pic1.shape[0], pic1.shape[1] * 3,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap(image)
        self.pic.setPixmap(pix)
        
        

        '''

      #--------------- set position preview ---------------------------------------
        
        
        width2 = 400
        height2 = 400
        self.picc = QtGui.QLabel(self)
        self.picc.setGeometry(800, 50,  640, 480)
        
        
        self.picc1 = QtGui.QLabel(self)
        self.picc1.setGeometry(150, 50,  width2, height2)
        #self.picc1.setPixmap(pix2)






        

        

        
       
        #---------------------------BUTTON-------------------------------------

        btn_start = QtGui.QPushButton("Start",self)
        btn_start.clicked.connect(self.actions_manual)
        btn_start.resize(400,100)
        btn_start.move(100,750)

        
        '''
        btn_start = QtGui.QPushButton("Ready", self)
        btn_start.clicked.connect(self.actions_ready)
        btn_start.resize(100,30)
        btn_start.move(330,150)
        '''


        self.show()
    
    #----------------------------------ACTION FUNCTIONS---------------------------
    def actions_home(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        print("Home Start",buadrate,comport) 

    def actions_ready(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        print("Ready Start",buadrate,comport) 


    def actions_auto(self):
        buadrate = self.text_br.text()
        comport = self.text_port.text()
        print("Auto Start",buadrate,comport)  

    def actions_manual(self):
        self.number = 0
        self.timer =  QtCore.QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(20)
        

        
        
                    
    def update(self):
        pix = 0
        #self.result.setText(str(self.number))
        
        if self.number<=199:
                pic3 = "test7\\data1\\"+str(self.number)+".jpg"
                pic4,width2,height2 = self.cvt_image(pic3,400,400)
                self.picc1.setPixmap(pic4)
        else :
            self.timer.stop()
            U = Cooretion.Coore()
            pic5 = "test7\\save1\\2.jpg"
            pic6,width3,height = self.cvt_image(pic5,640,480)
            self.picc.setPixmap(pic6)
            
            if U>=0.6 :
                
                self.result.setText("Contamination")
                
            else :
                self.result.setText("Non-Contamination  ")


        

            
            

            
        
        
        self.number+=1
     





    def cvt_image(self,photo,width,height):
        
        picx = cv2.imread(photo)
        dim = (width, height)
        pic1 = cv2.resize(picx, dim, interpolation = cv2.INTER_AREA)
        image = QtGui.QImage(pic1, pic1.shape[1],pic1.shape[0], pic1.shape[1] * 3,QtGui.QImage.Format_RGB888)
        pix = QtGui.QPixmap(image)
      
        return pix,width,height

        

        
        
        


def run():
    app = QtGui.QApplication(sys.argv)
    GUI = Window()
    sys.exit(app.exec_())




run()

