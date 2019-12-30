from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow

from list_all_reports import Ui_MainWindow
from ticket_info_function import ticket_info


class list_of_all_reports(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(list_of_all_reports, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.tableWidget_2.doubleClicked.connect(self.clicked_row)
        self.ticket_info = ticket_info()

    def clicked_row(self):
        row = self.tableWidget_2.currentRow()
        ls = []
        self.ticket_info = ticket_info()
        for i in range(6):
            ls.append(self.tableWidget_2.item(row, i).text())
        print(ls)

        self.ticket_info.show_ticket_info_list(ls)
        self.ticket_info.show()

    def show_tickets_info(self, result):
        for row_num, row_data in enumerate(result):
            self.tableWidget_2.insertRow(row_num)

            for col_num, data in enumerate(row_data):
                self.tableWidget_2.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(row_data[data])))
