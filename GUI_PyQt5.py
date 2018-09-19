# Getting some expirience with PyQt5
# Example code from ZetCode Authored by Jan Bodnar (August 2017) was used
# See: http://zetcode.com/gui/pyqt5/firstprograms/

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QIcon

class NewWindow(QWidget):
    def __init__(self):
        super().__init__()
                     
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
        
class Example(QWidget):  
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        # Instead of resize() and move(), setGeometry() can be used to set both
        #self.setGeometry(300, 300, 300, 220)
                     
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
        btn.move(0, 0)  
        
        btn2 = QPushButton("Toggle Window", self)
        btn2.move(0, 50)
        btn2.clicked.connect(self.buttonClicked)
        
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

if __name__ == '__main__':
    
    # Create application object
    app = QApplication(sys.argv)
    ex = Example()
    # Enter the app mainloop
    sys.exit(app.exec_())