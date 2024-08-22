import sys
import os
import re

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import QRect

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

class Validation():

    @staticmethod
    def license_plates(plate):
        valid_plate_pattern = r"^[a-z]{3}-[0-9]{3}$"
        return bool(re.fullmatch(valid_plate_pattern, plate, re.IGNORECASE))


class ManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Komunalai")

        central_w = QWidget()
        self.setCentralWidget(central_w)
        self.setGeometry(1000, 300, 200, 250)

        vbox = QVBoxLayout(central_w)
        hbox = QHBoxLayout(central_w)

        # Elektra
        self.electricity_label = QLabel(self)
        self.electricity_label.setText("Elektra:")

        self.electricity_value_from = QLineEdit(self)
        self.electricity_value_to = QLineEdit(self)
        self.electricity_rate = QLineEdit(self)

        self.electricity_value_from.setPlaceholderText("Nuo")
        self.electricity_value_to.setPlaceholderText("Iki")
        self.electricity_rate.setPlaceholderText("Tarifas")
        
        # Dujos
        self.gas_label = QLabel(self)
        self.gas_label.setText("Dujos:")

        self.gas_value_from = QLineEdit(self)
        self.gas_value_to = QLineEdit(self)
        self.gas_rate = QLineEdit(self)

        self.gas_value_from.setPlaceholderText("Nuo")
        self.gas_value_to.setPlaceholderText("Iki")
        self.gas_rate.setPlaceholderText("Tarifas")
        
        # Saltas
        self.cold_h2o_label = QLabel(self)
        self.cold_h2o_label.setText("Šaltas H2O:")

        self.cold_h2o_value_from = QLineEdit(self)
        self.cold_h2o_value_to = QLineEdit(self)
        self.cold_h2o_rate = QLineEdit(self)

        self.cold_h2o_value_from.setPlaceholderText("Nuo")
        self.cold_h2o_value_to.setPlaceholderText("Iki")
        self.cold_h2o_rate.setPlaceholderText("Tarifas")

        # Karstas
        self.hot_h2o_label = QLabel(self)
        self.hot_h2o_label.setText("Karštas H2O:")

        self.hot_h2o_value_from = QLineEdit(self)
        self.hot_h2o_value_to = QLineEdit(self)
        self.hot_h2o_rate = QLineEdit(self)

        self.hot_h2o_value_from.setPlaceholderText("Nuo")
        self.hot_h2o_value_to.setPlaceholderText("Iki")
        self.hot_h2o_rate.setPlaceholderText("Tarifas")

        self.submit_btn = QPushButton("Išsiųsti", self)


        vbox.addWidget(self.electricity_label)
        vbox.addWidget(self.electricity_value_from)
        vbox.addWidget(self.electricity_value_to)
        vbox.addWidget(self.electricity_rate)
        
        vbox.addWidget(self.gas_label)
        vbox.addWidget(self.gas_value_from)
        vbox.addWidget(self.gas_value_to)
        vbox.addWidget(self.gas_rate)
        
        vbox.addWidget(self.cold_h2o_label)
        vbox.addWidget(self.cold_h2o_value_from)
        vbox.addWidget(self.cold_h2o_value_to)
        vbox.addWidget(self.cold_h2o_rate)

        vbox.addWidget(self.hot_h2o_label)
        vbox.addWidget(self.hot_h2o_value_from)
        vbox.addWidget(self.hot_h2o_value_to)
        vbox.addWidget(self.hot_h2o_rate)

        vbox.addWidget(self.submit_btn)


# separate validations in class
# main class which runs windows
def main():
    app = QApplication(sys.argv)

    management_window = ManagementWindow()
    management_window.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
