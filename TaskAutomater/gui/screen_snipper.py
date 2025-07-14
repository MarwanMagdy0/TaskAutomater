import sys
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtGui import QPixmap, QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QPoint, QRect, pyqtSignal


class FullscreenSnipper(QLabel):
    imageCropped = pyqtSignal(QPixmap)
    def __init__(self):
        super().__init__()
        screen = app.primaryScreen()
        screenshot = screen.grabWindow(0)
        self.setPixmap(screenshot)
        self.origin = QPoint()
        self.end = QPoint()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setWindowState(Qt.WindowFullScreen)
        self.setCursor(Qt.CrossCursor)

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.end = self.origin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.end = event.pos()
        rect = QRect(self.origin, self.end).normalized()
        cropped = self.pixmap().copy(rect)
        self.imageCropped.emit(cropped)
        self.close()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        painter.setPen(QPen(QColor(0, 120, 215), 2))
        painter.setBrush(QColor(0, 120, 215, 40))
        painter.drawRect(QRect(self.origin, self.end).normalized())



if __name__ == "__main__":
    app = QApplication(sys.argv)

    snipper = FullscreenSnipper()
    snipper.show()

    sys.exit(app.exec_())