# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

import cv2 as cv
import numpy as np
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QImage, QPixmap
from sharedMemory import openSharedMemory

# Frame resolutions
WIDTH = 720
ROWBYTES = 1440
HEIGHT = 576

# W x H = 720x576
# Bytes W x Bytes H = 1440 x 576
# This means that 576 rows, each row has 1440 bytes YUV 4:2:2 raw byte data

# Convert YUV4:2:2 to RGB
# yuvData is the mmap object to the shared memory from C++ capture
def YUV422toBGR(yuvData, width, height):
    yuvFrameRAW = np.frombuffer(yuvData, dtype=np.uint8, count = -1, offset = 0) # Create 1D array of raw yuv data
    yuvFrameRAW = yuvFrameRAW.reshape((height, width * 2)) # Reshape into 2D array
    yuvFrameRAW = yuvFrameRAW.reshape((height, width, 2)) # Reshape into 2 channels per pixel
    bgrFrame = cv.cvtColor(yuvFrameRAW, cv.COLOR_YUV2BGR_UYVY) # Convert YUV to BGR
    return bgrFrame

class MainWindow(QMainWindow):

    def updateFrame(self):
        # Get shared frame
        yuvData = self.sharedMemory

        width = WIDTH
        height = HEIGHT

        # Convert YUV to BGR
        bgrFrame = YUV422toBGR(yuvData, width, height)

        height, width, _ = bgrFrame.shape
        bytes_per_line = width * 3  # 3 bytes per pixel in BGR
        q_image = QImage(bgrFrame.data, width, height, bytes_per_line, QImage.Format_BGR888)
        self.preview_label.setPixmap(QPixmap.fromImage(q_image))

        #TODO: replace timer with interrupt when the frame is ready
        QTimer.singleShot(20, self.updateFrame)


    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Use the shared memory function
        try:
            self.sharedMemory = openSharedMemory()
            print("Shared memory opened successfully!")
        except OSError as e:
            print(f"Error: {e}")

        # Access the previewContainer from the UI
        self.preview_label = QLabel(self.ui.previewContainer)
        self.preview_label.setAlignment(Qt.AlignCenter)
        self.updateFrame()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
