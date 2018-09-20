# Getting some expirience with PyQt5
# Example code from ZetCode Authored by Jan Bodnar (August 2017) was used
# See: http://zetcode.com/gui/pyqt5/firstprograms/

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

class SliderWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Setup of slider
        slider = QSlider(Qt.Horizontal, self)
        slider.setMinimum(20)
        slider.setMaximum(140)
        
        # Setup of number display
        lcd = QLCDNumber()
        slider.valueChanged.connect(lcd.display)
        
        slider.setValue(80)
                
        layout = QVBoxLayout()
        layout.addWidget(lcd)
        layout.addWidget(slider)
        
        # Set size of the window
        self.resize(300, 350)
        # Set position on the screen
        self.move(50, 50)
        self.setWindowTitle('Slider Window')
        
        self.setLayout(layout)
        
class NewWindow(QWidget):
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
        vbox.addWidget(self.lcd)
        vbox.addWidget(label1)
        self.setLayout(vbox)
        
        # Set size of the window
        self.resize(400, 150)
        # Set position on the screen
        self.move(400, 400)
        self.setWindowTitle('New window')
        self.setWindowIcon(QIcon('web.png'))
        
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
        
class Example(QWidget):  
    sliderW = 0
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # Instead of resize() and move(), setGeometry() can be used to set both
        #self.setGeometry(300, 300, 300, 220)
                  
        self.sliderW = SliderWindow()
                           
        # Set size of the window
        self.resize(250, 150)
        # Set position on the screen
        self.move(300, 300)
        self.setWindowTitle('My PyQt5 GUI')
        self.setWindowIcon(QIcon('web.png'))
        
        # Create pushbutton that closes the window
        btn = QPushButton('Exit', self)
        btn.clicked.connect(QApplication.instance().quit)
        btn.resize(btn.sizeHint())
        
        btn2 = QPushButton("Toggle Window", self)
        btn2.clicked.connect(self.buttonClicked)
        
        btn3 = QPushButton("Show Slider", self)
        btn3.clicked.connect(self.openSlider)
        
        plus = QPushButton("+", self)
        plus.clicked.connect(self.add)
        
        minus = QPushButton("-", self)
        minus.clicked.connect(self.subtract)
        
        # Create box layout and add elements to it
        vbox = QVBoxLayout()
        vbox.addWidget(plus)
        vbox.addWidget(minus)
        vbox.addWidget(btn3)
        vbox.addWidget(btn2)
        vbox.addWidget(btn)
        self.setLayout(vbox)
        
        self.dialog = NewWindow()
        
        # Show the already created window now on screen
        self.show()
    
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
                    
    def add(self):
        self.dialog.add()
        
    def subtract(self):
        self.dialog.subtract()
        
if __name__ == '__main__':
    
    # Create application object
    app = QApplication(sys.argv)
    ex = Example()
    # Enter the app mainloop
    sys.exit(app.exec_())