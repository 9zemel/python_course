import sys
from PyQt5.QtWidgets import QApplication
from  PyQt5.QtWidgets import QLabel
from  PyQt5.QtWidgets import QWidget

app = QApplication(sys.argv)
#sys argy дает возможность принимать аргументы из командной строки
#можно оставить скобоки пустыми
window = QWidget()

window.setWindowTitle('FirstApp')

window.setGeometry(90,90,300,300)
#x,y где окно появится: 300x300 размерность окна
window.move(60,15)
#двигаемся по x и y, где будет отрисовка виджета
helloMsg = QLabel('<h1>Привет</h1>', parent = window)
helloMsg.resize(300,300)
helloMsg.move(60,15)
window.move(60,50)
helloSecondMsg = QLabel('<h3>Как дела</h3>', parent = window)
helloSecondMsg.move(60,50)

window.show()

sys.exit(app.exec())


