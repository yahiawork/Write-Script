from PyQt5.QtWidgets import QApplication
from assets.Trans import translate
from PyQt5.QtGui import QIcon

class Main(translate):
    def __init__(self):
        super().__init__()
        self.setWindowIcon(QIcon('assets\icon\icon.png'))

if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    window.show() 
    app.exec_()