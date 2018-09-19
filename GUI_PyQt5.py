# Getting some expirience with PyQt5
# Example code from ZetCode Authored by Jan Bodnar (August 2017) was used
# See: http://zetcode.com/gui/pyqt5/firstprograms/

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget

if __name__ == '__main__':
    
    # Create application object
    app = QApplication(sys.argv)

    # Create widget without any parameters: a window
    w = QWidget()
    # Set size of the window
    w.resize(250, 150)
    # Set position on the screen
    w.move(300, 300)
    w.setWindowTitle('My PyQt5 GUI')
    # Show the already created window now on screen
    w.show()

    # Enter the app mainloop
    sys.exit(app.exec_())