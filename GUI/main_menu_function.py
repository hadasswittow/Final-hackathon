from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic.properties import QtWidgets

import search_ticket_function
import ticket_info
import ticket_info_function
from dbquerey import get_all_reports
from list_of_all_reports_function import list_of_all_reports
from main_menu import Ui_MainWindow

class main_menu(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(main_menu, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.list_of_all_reports = list_of_all_reports()
        self.pushButton.clicked.connect(self.sreach_reports)
        self.pushButton_4.clicked.connect(self.all_reports)



    def sreach_reports(self):
        self.ui = search_ticket_function.search_ticket()
        self.ui.show()

    def all_reports(self):
        result = get_all_reports()
        self.list_of_all_reports.show_tickets_info(result)
        self.list_of_all_reports.show()



if __name__ == '__main__':
    app = QApplication([])
    print("hi")
    app.setApplicationName("cut_the_line")
    window = main_menu()
    window.show()

    app.exec_()
