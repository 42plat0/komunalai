from PyQt5.QtWidgets import (
    QWidget,
    QPushButton,
    QMainWindow,
    QGridLayout,
    QLabel,
    QLineEdit,
)
from PyQt5 import QtCore

from calculator.calc import UtilitiesCalc
from file.json_maker import *

class ManagementWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.calc_wind()
    
    def get_last_log(self):
        j = read_json_file()
        j = get_dict_f_json(j)
        last_log_key = list(j.keys())[len(j.keys()) - 1]
        last_log = j[last_log_key] 
        return last_log


    def calc_wind(self):
        self.setWindowTitle("Komunalai")
        central_w = QWidget()
        self.setCentralWidget(central_w)
        self.setGeometry(700, 300, 500, 250)

        grid = QGridLayout(central_w)

        # Last log if it exists
        log = None
        if log_exists():
            log = self.get_last_log()

        # Elektra
        self.electricity_label = QLabel(self)
        self.electricity_label.setText("Elektra:")

        # Inserts previous month values
        if log:
            self.electricity_value_from = QLineEdit(log["el"]["to"])
            self.electricity_value_to = QLineEdit(self)
            self.electricity_rate  = QLineEdit(log["el"]["rate"])
            self.electricity_fixed = QLineEdit(log["el"]["fixed"])
        else:
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

        # Inserts previous month values
        if log:
            self.gas_value_from = QLineEdit(log["gas"]["to"])
            self.gas_value_to = QLineEdit(self)
            self.gas_rate  = QLineEdit(log["gas"]["rate"])
            self.gas_fixed  = QLineEdit(log["gas"]["fixed"])
        else:
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

        # Inserts previous month values
        if log:
            self.cold_h2o_value_from = QLineEdit(log["cold_h2o"]["to"])
        else:
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

        # Inserts previous month values
        if log:
            self.hot_h2o_value_from = QLineEdit(log["hot_h2o"]["to"])
        else:
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
        # Inserts previous month values
        if log:
            self.admin_pay_val = QLineEdit(str(log["admin"]["pay_val"]))
        else:
            self.admin_pay_val  = QLineEdit(self)
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
        # Inserts previous month values
        if log:
            self.rent_pay_val = QLineEdit(str(log["rent"]["pay_val"]))
        else:
            self.rent_pay_val  = QLineEdit(self)

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
        self._save_utility_log()
        for u_name, u_vals in self.uc.utils.items():
            self.u_label = QLabel(self)
            self.u_label.setText(u_name.upper() + "\n-----------")
            self.u_label.setAlignment(QtCore.Qt.AlignCenter)

            self.u_vals = QLabel(self)
            self.u_vals.setText(
                f"Nuo {u_vals["from"] if u_vals["from"] else "-"}"
                + f"\nIki {u_vals["to"] if u_vals["to"] else "-"}"
                + f"\nSkirtumas {u_vals["diff"] if u_vals["diff"] else "-"}"
                + f"\nMoketi: {u_vals["pay_val"]}"
            )
            self.u_vals.setAlignment(QtCore.Qt.AlignCenter)

            grid.addWidget(self.u_label)
            grid.addWidget(self.u_vals)

        total = self.uc.get_total()
        for_each = self.uc.get_for_each()

        self.pay_label = QLabel(self)
        self.pay_label.setText(f"----\nViso {total}\nKiekvienam {for_each}")
        self.pay_label.setAlignment(QtCore.Qt.AlignCenter)

        grid.addWidget(self.pay_label)

    def _save_utility_log(self):
        log = self.uc.get_saveable_dict()# Get content log

        if log_exists():
            f_content = read_json_file()
            f_content = get_dict_f_json(f_content)
            update_dct(f_content, log)
            f_content = form_json(f_content) 
            write_json_file(f_content)
        else:
            log = form_json(log)
            write_json_file(log)

    def _set_utilities(self):
        self.uc = UtilitiesCalc(2)

        self.uc.add_util(
            "el",
            self.electricity_value_from.text(),
            self.electricity_value_to.text(),
            self.electricity_rate.text(),
            self.electricity_fixed.text(),
        )
        self.uc.add_util(
            "gas",
            self.gas_value_from.text(),
            self.gas_value_to.text(),
            self.gas_rate.text(),
            self.gas_fixed.text(),
        )
        self.uc.add_util(
            "cold_h2o",
            self.cold_h2o_value_from.text(),
            self.cold_h2o_value_to.text(),
            self.cold_h2o_rate.text(),
            u_pay_val=self.cold_h2o_pay_val.text(),
        )
        self.uc.add_util(
            "hot_h2o",
            self.hot_h2o_value_from.text(),
            self.hot_h2o_value_to.text(),
            self.hot_h2o_rate.text(),
            u_pay_val=self.hot_h2o_pay_val.text(),
        )

        self.uc.add_util("admin", u_pay_val="28.87")
        self.uc.add_util("rent", u_pay_val=self.rent_pay_val.text())
