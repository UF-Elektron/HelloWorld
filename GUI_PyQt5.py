#-----------------------------------------------------------------------------
# Project:        Qt with Python! 
# Description:    Getting some expirience with PyQt5
# Author:         David Müller
# Date:           September 2018
#-----------------------------------------------------------------------------
# Note: Example code from ZetCode Authored by Jan Bodnar (August 2017) was used
# See: http://zetcode.com/gui/pyqt5/firstprograms/
#-----------------------------------------------------------------------------

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QLCDNumber
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QImage, QImageWriter, QImageIOHandler
from PyQt5.Qt import QPixmap

class ImageWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Image Window')

        # Create label and add pixmap to it
        self.myLabel = QLabel(self)
        myPixmap = QPixmap('testImage.png')
        self.myLabel.setPixmap(myPixmap)
        
        # Create pushbuttons
        #-------------------
        # Create pushbutton to rotate image left
        btnRotateL = QPushButton('Rotate 90° left', self)
        btnRotateL.clicked.connect(self.rotateL)
        
        # Create pushbutton to rotate image left
        btnRotateR = QPushButton('Rotate 90° right', self)
        btnRotateR.clicked.connect(self.rotateR)
        
        # Create pushbutton to mirror image hirizontally
        btnMirror = QPushButton('Mirror horizontally', self)
        btnMirror.clicked.connect(self.mirror)
                
        # Create box layout and add elements to it
        vbox = QVBoxLayout()
        vbox.addWidget(btnRotateL)
        vbox.addWidget(btnRotateR)
        vbox.addWidget(btnMirror)
        vbox.addWidget(self.myLabel)
        self.setLayout(vbox)
        
        # Set window size to match size of pixmap
        self.resize(myPixmap.width(),myPixmap.height())

        print('Image window initialized')

    def rotateL(self):
        # Load image for QImageWriter
        self.myImg = QImageWriter('testImage.png')
        # Rotate image with QImageWriter transformation function
        self.myImg.setTransformation(QImageIOHandler.TransformationRotate270)
               
        self.updateImage()
    
    def rotateR(self):
        # Load image for QImageWriter
        self.myImg = QImageWriter('testImage.png')
        # Rotate image with QImageWriter transformation function
        self.myImg.setTransformation(QImageIOHandler.TransformationRotate90)
        
        self.updateImage()

    def mirror(self):
        # Load image for QImageWriter
        self.myImg = QImageWriter('testImage.png')
        # Rotate image with QImageWriter transformation function
        self.myImg.setTransformation(QImageIOHandler.TransformationMirror)
        
        self.updateImage()
          
    def updateImage(self):
        newImage = QImage('testImage.png')
        errorValue = self.myImg.write(newImage)
        if errorValue == 0:
            print('Error, image was not saved!') 
        myPixmap = QPixmap('testImage.png')
        self.myLabel.setPixmap(myPixmap)
        
class SliderWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        sliderMin = 20
        sliderMax = 140
                
        # Setup of slider
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(sliderMin)
        slider.setMaximum(sliderMax)
        
        # Setup of number display
        lcd = QLCDNumber()
        slider.valueChanged.connect(lcd.display)
        
        slider.setValue((sliderMin + sliderMax) / 2)
                
        layout = QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        
        # Set size of the window
        self.resize(300, 350)
        # Set position on the screen
        self.move(50, 50)
        self.setWindowTitle('Slider Window')
        
        self.setLayout(layout)
        print('Slider window initialized. Init val =', slider.value())
         
class CounterWindow(QWidget):
    myCounter = 0
    lcd = 0
    
    def __init__(self):
        super().__init__()

        label1 = QLabel('Counter value:', self)
        self.lcd = QLCDNumber(self)
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.display(self.myCounter)
        
        # Create box layout and add elements to it
        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(self.lcd)
        self.setLayout(vbox)
        
        # Set size of the window
        self.resize(400, 150)
        # Set position on the screen
        self.move(400, 400)
        self.setWindowTitle('New window')
        self.setWindowIcon(QIcon('web.png'))
        print('Counter window initialized')
        
    # Return current state of this window
    def getWindowState(self):
        print('Visibility = ', self.isVisible())
        return self.isVisible()
        
    # Increment counter and update LCD in window
    def add(self):
        self.myCounter = self.myCounter + 1
        self.lcd.display(self.myCounter)
        print(self.myCounter)
        
    # Decrement counter and update LCD in window   
    def subtract(self):
        self.myCounter = self.myCounter - 1
        self.lcd.display(self.myCounter)
        print(self.myCounter)
        
class MainWindow(QWidget):  
    sliderW = 0
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Instead of resize() and move(), setGeometry() can be used to set both
        #self.setGeometry(300, 300, 300, 220)
                  
        # Initialize slider window
        self.sliderW = SliderWindow()
                           
        # Initialize counter window
        self.dialog = CounterWindow()
        
        # Initialize image window
        self.imageW = ImageWindow()

        # Set size of the window
        self.resize(250, 150)
        # Set window position on screen
        self.move(300, 300)
        self.setWindowTitle('My PyQt5 GUI')
        self.setWindowIcon(QIcon('web.png'))
        
        # Create pushbuttons
        #-------------------
        # Create pushbutton that closes the window
        btnExit = QPushButton('Exit', self)
        btnExit.clicked.connect(QApplication.instance().quit)
        btnExit.resize(btnExit.sizeHint())
        
        # Create pushbutton that toggles a window with a counter
        btnToggle = QPushButton("Toggle Window", self)
        btnToggle.clicked.connect(self.buttonClicked)
        
        # Create pushbutton that shows a window with a slider
        btnSlider = QPushButton("Show Slider", self)
        btnSlider.clicked.connect(self.openSlider)
        
        # Create pushbutton: show image
        btnImage = QPushButton("Image", self)
        btnImage.clicked.connect(self.showImage)
        
        # Create pushbutton to increment a value
        btnPlus = QPushButton("+", self)
        btnPlus.clicked.connect(self.add)
        
        # Create pushbutton to decrement a value
        btnMinus = QPushButton("-", self)
        btnMinus.clicked.connect(self.subtract)
        
        # Create box layout and add elements to it
        vbox = QVBoxLayout()
        vbox.addWidget(btnPlus)
        vbox.addWidget(btnMinus)
        vbox.addWidget(btnSlider)
        vbox.addWidget(btnToggle)
        vbox.addWidget(btnImage)
        vbox.addWidget(btnExit)
        self.setLayout(vbox)
        
        # Show the already created window now on screen
        self.show()
        print('Main window initialized')
    
    # Ask for confirmation on closeEvent (press of X in window title)
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm closeEvent',
            "Are you sure to quit?", QMessageBox.Yes | 
            QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    
    def buttonClicked(self):
        if self.dialog.getWindowState():
            self.dialog.close()
        else:
            self.dialog.show()
    
    def openSlider(self):
        self.sliderW.show()
    
    def showImage(self):
        self.imageW.show()
                      
    def add(self):
        self.dialog.add()
        
    def subtract(self):
        self.dialog.subtract()
        
if __name__ == '__main__':
    
    # Create application object
    app = QApplication(sys.argv)
    ex = MainWindow()
    # Enter the app mainloop
    sys.exit(app.exec_())
