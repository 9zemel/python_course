import sys
import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtWidgets import QPushButton

def greeting():
    if msg.text():
        msg.setText('')
    else:
        msg.setText(str(random.randint(0,100)))

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('`Сигналы и слоты')
layout = QVBoxLayout()

btn = QPushButton('hi')
btn.clicked.connect(greeting)

layout.addWidget(btn)
msg = QLabel('')

layout.addWidget(msg)
window.setWindowTitle()


