import sys
import os

from client.client import ManagementWindow
from PyQt5.QtWidgets import QApplication

WORKING_DIR = os.path.dirname(os.path.abspath(__file__))

# separate validations in class
# main class which runs windows
def main():
    app = QApplication(sys.argv)

    management_window = ManagementWindow()
    management_window.show()

    sys.exit(app.exec_())
    pass


if __name__ == "__main__":
    main()

