import sys
import os
import re

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QGridLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import QRect, Qt

"""
    TODO's 
    
        1. Parasyti funkcija, kuri suskaiciuotu pagal tarifa ir ar pastovu rate sumas ir jas sudetu i dictionary
        2. Funkcija patalpinti i klase (Galbut atskira) ir integruoti i window kalse
        3. Pagaminti excelio faila suformatuota is gautu duomenu
        
        Papildomos idejos (TODO):

            -. Issiusti emaila su attachmentu Nuomininkui
            -. Padaryti pavedima issiuntus attachmenta
            -. Config failas, kuriuo pasirenkami laukeliai, pavadinimas failu, direktorija, emailas etc..
"""

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

class Validation():

    @staticmethod
    def license_plates(plate):
        valid_plate_pattern = r"^[a-z]{3}-[0-9]{3}$"
        return bool(re.fullmatch(valid_plate_pattern, plate, re.IGNORECASE))


class ManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        fields = ["from", "to", "rate", "fixed"]

        self.setWindowTitle("Komunalai")

        central_w = QWidget()
        self.setCentralWidget(central_w)
        self.setGeometry(700, 300, 500, 250)

        grid = QGridLayout(central_w)
        

        # Elektra
        self.electricity_label = QLabel(self)
        self.electricity_label.setText("Elektra:")

        self.electricity_value_from = QLineEdit(self)
        self.electricity_value_to = QLineEdit(self)
        self.electricity_rate = QLineEdit(self)
        self.electricity_fixed = QLineEdit(self)

        self.electricity_value_from.setPlaceholderText("Nuo")
        self.electricity_value_to.setPlaceholderText("Iki")
        self.electricity_rate.setPlaceholderText("Tarifas")
        self.electricity_fixed.setPlaceholderText("Pastovus")
        
        # Dujos
        self.gas_label = QLabel(self)
        self.gas_label.setText("Dujos:")

        self.gas_value_from = QLineEdit(self)
        self.gas_value_to = QLineEdit(self)
        self.gas_rate = QLineEdit(self)
        self.gas_fixed = QLineEdit(self)

        self.gas_value_from.setPlaceholderText("Nuo")
        self.gas_value_to.setPlaceholderText("Iki")
        self.gas_rate.setPlaceholderText("Tarifas")
        self.gas_fixed.setPlaceholderText("Pastovus")
        
        # Saltas
        self.cold_h2o_label = QLabel(self)
        self.cold_h2o_label.setText("Šaltas H2O:")

        self.cold_h2o_value_from = QLineEdit(self)
        self.cold_h2o_value_to = QLineEdit(self)
        self.cold_h2o_rate = QLineEdit(self)
        self.cold_h2o_fixed = QLineEdit(self)

        self.cold_h2o_value_from.setPlaceholderText("Nuo")
        self.cold_h2o_value_to.setPlaceholderText("Iki")
        self.cold_h2o_rate.setPlaceholderText("Tarifas")
        self.cold_h2o_fixed.setPlaceholderText("Pastovus")

        # Karstas
        self.hot_h2o_label = QLabel(self)
        self.hot_h2o_label.setText("Karštas H2O:")

        self.hot_h2o_value_from = QLineEdit(self)
        self.hot_h2o_value_to = QLineEdit(self)
        self.hot_h2o_rate = QLineEdit(self)
        self.hot_h2o_fixed = QLineEdit(self)

        self.hot_h2o_value_from.setPlaceholderText("Nuo")
        self.hot_h2o_value_to.setPlaceholderText("Iki")
        self.hot_h2o_rate.setPlaceholderText("Tarifas")
        self.hot_h2o_fixed.setPlaceholderText("Pastovus")

        # Nuoma
        self.rent_label = QLabel(self)
        self.rent_label.setText("Nuoma")

        self.rent_value_from = QLineEdit(self)
        self.rent_value_to = QLineEdit(self)
        self.rent_rate = QLineEdit(self)
        self.rent_fixed = QLineEdit(self)
        
        self.rent_value_from.setEnabled(False), self.rent_value_to.setEnabled(False), self.rent_rate.setEnabled(False)
        
        self.rent_value_from.setPlaceholderText("-")
        self.rent_value_to.setPlaceholderText("-")
        self.rent_rate.setPlaceholderText("-")
        self.rent_fixed.setPlaceholderText("Pastovus")

        self.submit_btn = QPushButton(self)
        self.submit_btn.setText("Issiusti")

        # Create widgets to add to layout dynamically
        widgets = dict()
        for item in self.__dict__:
            if "btn" not in item: # Add button individually
                widgets[item.split("_")[0]] = []
        else:
            for item, obj in self.__dict__.items():
                if "btn" not in item: # Add button individually
                    widgets[item.split("_")[0]].append(obj)

        row = 0
        for widget, obj_lst in widgets.items():
            col = 0
            for obj in obj_lst:
                grid.addWidget(obj, row, col)
                col += 1
            
            row +=1
        
        grid.addWidget(self.submit_btn, row, int(row/2), 1, 1)


# separate validations in class
# main class which runs windows
def main():
    # app = QApplication(sys.argv)

    # management_window = ManagementWindow()
    # management_window.show()

    # sys.exit(app.exec_())
    pass


if __name__ == "__main__":
    main()


utils = [
    ("electricity", {
        "from": "0010697.0",
        "to": "0010739.0",
        "rate": "0.214",
        "fixed": None
    }),

    ("gas", {
        "from": "01488000",
        "to" : "01490457",
        "rate": "1.4",
        "fixed": "0.56"
    }),

    ("hot_h2o", {
        "from": "0622000",
        "to": "0622895",
        "rate": None,
        "fixed": None
    }),

    ("cold_h2o", {
        "from": "05360000",
        "to":   "00539999",
        "rate": None,
        "fixed": None
    })
]

def calculate_utils():
    params = ("from", "to", "rate", "fixed")

    for util in utils:
        util_name = util[0]
        util_params = util[1]
        
        for param in params:
            util_param = util_params[param]
            if util_param is not None:
                param_to_number = float(util_params[param].lstrip("0"))


print(calculate_utils())
