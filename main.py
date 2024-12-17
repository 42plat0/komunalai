import sys
import os
import re

from client.client import ManagementWindow
from PyQt5.QtWidgets import QApplication

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

