from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from list_all_reports import Ui_MainWindow


class list_of_all_reports(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(list_of_all_reports, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def show_tickets_info(self, result):
        for row_num, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_num)
            # self.tableWidget_2.setItem(row_num, 0, QtWidgets.QTableWidgetItem(str(data)))

            for col_num, data in enumerate(row_data):
                print(data)
                self.tableWidget_2.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(row_data[data])))
