from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QMainWindow,
    QGridLayout,
    QLabel,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtGui import QPainter, QPixmap
from PyQt5.QtCore import QRect, Qt

from calculator.calc import UtilitiesCalc

class ManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calc_wind()

    def calc_wind(self):
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
        self.cold_h2o_pay_val = QLineEdit(self)

        self.cold_h2o_value_from.setPlaceholderText("Nuo")
        self.cold_h2o_value_to.setPlaceholderText("Iki")
        self.cold_h2o_rate.setPlaceholderText("-")
        self.cold_h2o_pay_val.setPlaceholderText("Moketi")

        self.cold_h2o_rate.setEnabled(False)

        # Karstas
        self.hot_h2o_label = QLabel(self)
        self.hot_h2o_label.setText("Karštas H2O:")

        self.hot_h2o_value_from = QLineEdit(self)
        self.hot_h2o_value_to = QLineEdit(self)
        self.hot_h2o_rate = QLineEdit(self)
        self.hot_h2o_pay_val = QLineEdit(self)

        self.hot_h2o_value_from.setPlaceholderText("Nuo")
        self.hot_h2o_value_to.setPlaceholderText("Iki")
        self.hot_h2o_rate.setPlaceholderText("-")
        self.hot_h2o_pay_val.setPlaceholderText("Moketi")
        
        self.hot_h2o_rate.setEnabled(False)


        # Laiptine
        self.admin_label = QLabel(self)
        self.admin_label.setText("Laiptine")

        self.admin_value_from = QLineEdit(self)
        self.admin_value_to = QLineEdit(self)
        self.admin_rate = QLineEdit(self)
        self.admin_pay_val = QLineEdit(self)

        self.admin_value_from.setEnabled(False), self.admin_value_to.setEnabled(
            False
        ), self.admin_rate.setEnabled(False)

        self.admin_value_from.setPlaceholderText("-")
        self.admin_value_to.setPlaceholderText("-")
        self.admin_rate.setPlaceholderText("-")
        self.admin_pay_val.setPlaceholderText("Moketi")

        # Nuoma
        self.rent_label = QLabel(self)
        self.rent_label.setText("Nuoma")

        self.rent_value_from = QLineEdit(self)
        self.rent_value_to = QLineEdit(self)
        self.rent_rate = QLineEdit(self)
        self.rent_pay_val = QLineEdit(self)

        self.rent_value_from.setEnabled(False), self.rent_value_to.setEnabled(
            False
        ), self.rent_rate.setEnabled(False)

        self.rent_value_from.setPlaceholderText("-")
        self.rent_value_to.setPlaceholderText("-")
        self.rent_rate.setPlaceholderText("-")
        self.rent_pay_val.setPlaceholderText("Moketi")

        self.submit_btn = QPushButton(self)
        self.submit_btn.setText("Apskaiciuoti")
        self.submit_btn.clicked.connect(self.log_wind)

        # Create widgets to add to layout dynamically
        widgets = dict()
        for item in self.__dict__:
            if "btn" not in item:  # Add button individually
                widgets[item.split("_")[0]] = []
        else:
            for item, obj in self.__dict__.items():
                if "btn" not in item:  # Add button individually
                    widgets[item.split("_")[0]].append(obj)

        row = 0
        for widget, obj_lst in widgets.items():
            col = 0
            for obj in obj_lst:
                grid.addWidget(obj, row, col)
                col += 1

            row += 1

        grid.addWidget(self.submit_btn, row, int(row / 2) - 1, 1, 1)

    def log_wind(self):
        central_w = QWidget()
        self.setCentralWidget(central_w)
        self.setGeometry(700, 300, 500, 250)

        grid = QGridLayout(central_w)
        self._set_utilities()
        for u_name, u_vals in self.uc.utils.items():
            self.u_label = QLabel(self)
            self.u_label.setText(u_name.capitalize() + f" - Nuo {u_vals["from"] if u_vals["from"] else "-"}" + f" - Iki {u_vals["to"] if u_vals["to"] else "-"}" + f" - Moketi: {u_vals["pay_val"]}")
            
            grid.addWidget(self.u_label) 

        total = self.uc.get_total()
        for_each = self.uc.get_for_each()

        self.pay_label = QLabel(self)
        self.pay_label.setText(f"Viso {total}, kiekvienam {for_each}") 
        grid.addWidget(self.pay_label)
               

    def _set_utilities(self):
        self.uc = UtilitiesCalc(2) 

        self.uc.add_util("electricity", self.electricity_value_from.text(), self.electricity_value_to.text(), self.electricity_rate.text(), self.electricity_fixed.text())
        self.uc.add_util("gas", self.gas_value_from.text(), self.gas_value_to.text(), self.gas_rate.text(), self.gas_fixed.text())
        self.uc.add_util("hot h2o", self.hot_h2o_value_from.text(), self.hot_h2o_value_to.text(), self.hot_h2o_rate.text(), u_pay_val= self.hot_h2o_pay_val.text())
        self.uc.add_util("cold h2o", self.cold_h2o_value_from.text(), self.cold_h2o_value_to.text(), self.cold_h2o_rate.text(), u_pay_val=self.cold_h2o_pay_val.text())
        self.uc.add_util("admin", u_pay_val="28.87" )
        self.uc.add_util("rent", u_pay_val=self.rent_pay_val.text())