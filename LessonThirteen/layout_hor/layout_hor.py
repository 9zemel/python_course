import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle('QHBoxLayout')
layout = QHBoxLayout()
layout.addWidget(QPushButton('Слева '))
layout.addWidget(QPushButton('По центру'))
layout.addWidget(QPushButton('Справа'))
window.setLayout(layout)
window.show()
sys.exit(app.exec_())
