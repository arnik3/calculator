from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout, \
    QLCDNumber
import sys


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(330, 400, 200, 280)
        self.setWindowTitle("Calculator")
        self.res = QLabel(self)
        self.res.setText(' Result:')
        self.res.move(4, 3)
        self.first = QLineEdit()
        self.first.setStyleSheet("background-color: white ")
        self.second = QLineEdit()
        self.second.setStyleSheet("background-color: white ")
        self.ce = QLineEdit()
        self.grid = QGridLayout()
        self.container = QWidget()
        self.container.setStyleSheet("background-color: lightgray ")
        self.container.setLayout(self.grid)
        self.setCentralWidget(self.container)

        self.buttonplus = QPushButton('+', self)
        self.buttonplus.clicked.connect(self.plusclicked)
        self.buttonplus.setStyleSheet("background-color: lightcyan")

        self.button_ce = QPushButton('CE', self)
        self.button_ce.clicked.connect(self.ce_clicked)
        self.button_ce.setStyleSheet("background-color: lightcyan ")

        self.buttonpercent = QPushButton('%', self)
        self.buttonpercent.clicked.connect(self.percentclicked)
        self.buttonpercent.setStyleSheet("background-color: lightcyan ")

        self.buttonstep = QPushButton('x^', self)
        self.buttonstep.clicked.connect(self.stepclicked)
        self.buttonstep.setStyleSheet("background-color: lightcyan ")

        self.buttonfractional = QPushButton('1/x', self)
        self.buttonfractional.clicked.connect(self.fractionalclicked)
        self.buttonfractional.setStyleSheet("background-color: lightcyan ")

        self.buttonminus = QPushButton('﹣', self)
        self.buttonminus.clicked.connect(self.minusclicked)
        self.buttonminus.setStyleSheet("background-color: lightcyan")

        self.buttondel = QPushButton('/', self)
        self.buttondel.clicked.connect(self.delclicked)
        self.buttondel.setStyleSheet("background-color: lightcyan ")

        self.buttonmult = QPushButton('*', self)
        self.buttonmult.clicked.connect(self.multclicked)
        self.buttonmult.setStyleSheet("background-color: lightcyan ")
        self.button_2 = QPushButton('x²', self)
        self.button_2.clicked.connect(self.clicked_2)
        self.button_2.setStyleSheet("background-color: lightcyan ")
        self.result = QLCDNumber(8)
        self.result.display(0)
        self.result.setStyleSheet("background-color: lightcyan ")
        self.result.setMaximumSize(900, 30)
        self.grid.addWidget(self.first, 2, 1)
        self.grid.addWidget(self.second, 2, 2)
        self.grid.addWidget(self.result, 1, 1)
        self.grid.addWidget(self.button_ce, 3, 1)
        self.grid.addWidget(self.buttonminus, 3, 3)
        self.grid.addWidget(self.buttondel, 4, 2)
        self.grid.addWidget(self.buttonmult, 4, 1)
        self.grid.addWidget(self.buttonstep, 4, 3)
        self.grid.addWidget(self.buttonpercent, 5, 1)
        self.grid.addWidget(self.buttonplus, 3, 2)
        self.grid.addWidget(self.buttonfractional, 5, 2)
        self.grid.addWidget(self.button_2, 5, 3)

    def plusclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext + secondtext)

    def minusclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext - secondtext)

    def clicked_2(self):
        firstText = float(self.first.text())
        self.result.display(firstText * firstText)

    def fractionalclicked(self):
        firsttext = float(self.first.text())
        self.result.display(1 / firsttext)

    def ce_clicked(self):
        self.result.display(0)

    def delclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second. text())

        self.result.display(firsttext / secondtext)

    def stepclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext ** secondtext)

    def multclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext * secondtext)

    def percentclicked(self):
        firsttext = float(self.first.text())
        secondtext = float(self.second.text())
        self.result.display(firsttext * (1 / 100) * secondtext)

if __name__ == "__main__":
     app = QApplication(sys.argv)
     ex = Calculator()
     ex.show()
     sys.exit(app.exec())