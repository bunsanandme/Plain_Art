from PyQt5.QtWidgets import QMainWindow, QApplication, QMenu, QMenuBar, QAction, QFileDialog, QColorDialog
from PyQt5.QtGui import QIcon, QImage, QPainter, QPen, QBrush
from PyQt5.QtCore import Qt, QPoint
import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PleinArt"
        top = 400
        left = 400
        width = 800
        height = 600

        self.setWindowTitle(title)
        self.setGeometry(top, left, width, height)

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.drawing = False
        self.brush_size = 2
        self.brush_color = Qt.black
        self.last_point = QPoint()

        main_menu = self.menuBar()
        file_menu = main_menu.addMenu("File")
        brush_size = main_menu.addMenu("Brush Size")
        brush_color = main_menu.addMenu("Brush Color")

        save_action = QAction("Save", self)
        save_action.setShortcut("Ctrl+S")
        file_menu.addAction(save_action)
        save_action.triggered.connect(self.save)

        clear_action = QAction("Clear", self)
        clear_action.setShortcut("Ctrl+C")
        file_menu.addAction(clear_action)
        clear_action.triggered.connect(self.clear)

        d_action = QAction("Decrease size", self)
        d_action.setShortcut("Ctrl+Q")
        brush_size.addAction(d_action)
        d_action.triggered.connect(self.decrease_pixel)

        i_action = QAction("Increase size", self)
        i_action.setShortcut("Ctrl+W")
        brush_size.addAction(i_action)
        i_action.triggered.connect(self.increase_pixel)

        px3_action = QAction("3px", self)
        brush_size.addAction(px3_action)
        px3_action.triggered.connect(self.threePixel)

        px5_action = QAction("5px", self)
        brush_size.addAction(px5_action)
        px5_action.triggered.connect(self.fivePixel)

        px7_action = QAction("7px", self)
        brush_size.addAction(px7_action)
        px7_action.triggered.connect(self.sevenPixel)

        px9_action = QAction("9px", self)
        brush_size.addAction(px9_action)
        px9_action.triggered.connect(self.ninePixel)

        choose_action = QAction("Choose color", self)
        choose_action.setShortcut("Ctrl+B")
        brush_color.addAction(choose_action)
        choose_action.triggered.connect(self.chooseColor)

    def chooseColor(self):
        self.brush_color = QColorDialog.getColor()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if (event.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False

    def paintEvent(self, event):
        canvas_painter = QPainter(self)
        canvas_painter.drawImage(self.rect(), self.image, self.image.rect())

    def save(self):
        file_path, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                   "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        if file_path == "":
            return
        self.image.save(file_path)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def threePixel(self):
        self.brush_size = 3

    def fivePixel(self):
        self.brush_size = 5

    def sevenPixel(self):
        self.brush_size = 7

    def ninePixel(self):
        self.brush_size = 9

    def increase_pixel(self):
        self.brush_size += 1

    def decrease_pixel(self):
        self.brush_size -= 1
