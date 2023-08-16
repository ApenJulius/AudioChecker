import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtCore import Qt, QEventLoop
from audioPlayer import AudioPlayer
import asyncio
from time import sleep
from threading import Thread
import threading
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.refreshFiles()

    def initUI(self):
        main_widget = QWidget()
        layout = QVBoxLayout()
        audioContainer = QVBoxLayout()
        self.audioContainer = audioContainer
        
        refreshButton = QPushButton("Refresh")
        refreshButton.clicked.connect(self.refreshFiles)

        layout.addWidget(refreshButton)
        layout.addLayout(audioContainer)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

    def refreshFiles(self):
        self.audioFileDict = AudioPlayer().sortFiles()

        # Removing layout start
        while self.audioContainer.count() > 0:
            item = self.audioContainer.takeAt(0)
            widget = item.widget()
            self.audioContainer.removeWidget(widget)
            widget.deleteLater()
        # Removing layout end
        for sound in self.audioFileDict:
            self.audioContainer.addWidget(PairWidget(sound, self.audioFileDict[sound]))
    


class PairWidget(QWidget):
    def __init__(self, label_text, audioObject=None):
        super().__init__()
        self.initUI(label_text)
        self.audioObject = audioObject

    def initUI(self, label_text):
        self.label_text = label_text

        label = QLabel(label_text)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        buttonLeft = QPushButton("Left")
        buttonCenter = QPushButton("Both")
        buttonRight = QPushButton("Right")

        layout = QVBoxLayout()
        layout.addWidget(label)

        button_layout = QHBoxLayout()
        
        button_layout.addWidget(buttonLeft)
        button_layout.addWidget(buttonCenter)
        button_layout.addWidget(buttonRight)
        layout.addLayout(button_layout)


        self.setLayout(layout)
        buttonCenter.clicked.connect(self.handleButtonClicked)
        buttonLeft.clicked.connect(self.handleButtonClicked)
        buttonRight.clicked.connect(self.handleButtonClicked)

    def handleButtonClicked(self):
        button_text = self.sender().text()

        try:
            AudioPlayer().playAudio(self.audioObject[button_text])
        except:
            return
    

       

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()