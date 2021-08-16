import painter as pnt
from PyQt5.QtWidgets import QApplication
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = pnt.Window()
    window.show()
    app.exec()
