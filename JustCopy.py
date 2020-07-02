import sys
from PyQt4 import QtCore, QtGui
from pykeyboard import PyKeyboard
from mainform import Ui_MainWindow
from time import sleep


class StartQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.clearButton.clicked.connect(self.clear)
        self.ui.goButton.clicked.connect(self.gocopy)
        
        self.kbd=PyKeyboard()


    def clear(self):
        self.ui.lineEdit.setText("")
        self.ui.spinBox.setProperty("value", 5)
    
    def gocopy(self):
        self.ui.goButton.setEnabled(False)
        self.ui.clearButton.setEnabled(False)
        QtGui.QApplication.processEvents()
        twait=self.ui.spinBox.value()
#         print twait
        sleep (twait)
        text=self.ui.lineEdit.text()
        for c in text:
            sleep(0.3)
#             self.kbd.press_key('q')
#             self.kbd.release_key('q')
            self.kbd.tap_key(str(c), 1, 0)

#         self.kbd.type_string(text, 1)
            
        self.ui.goButton.setEnabled(True)
        self.ui.clearButton.setEnabled(True)
        QtGui.QApplication.processEvents()
        #print text

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = StartQT4()
    myapp.show()
    sys.exit(app.exec_())
