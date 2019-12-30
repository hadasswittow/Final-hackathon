from PyQt5.QtWidgets import QMainWindow, QApplication, QRadioButton

from dbquerey import get_report_by_license, get_report_by_time, get_report_by_area, get_report
from list_of_all_reports_function import list_of_all_reports
from search_ticket import Ui_MainWindow
from ticket_info_function import ticket_info


class search_ticket(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(search_ticket, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.search)
        self.ticket_info = ticket_info()
        self.list_of_all_reports = list_of_all_reports()

    def search(self):
        self.list_of_all_reports = list_of_all_reports()

        if self.radioButton.isChecked():
            result = get_report_by_license(self.lineEdit.text())

        if self.radioButton_2.isChecked():
            result = get_report_by_time(self.lineEdit.text())

        if self.radioButton_3.isChecked():
            result = get_report_by_area(self.lineEdit.text())

        if self.radioButton_4.isChecked():
            result = get_report(self.lineEdit.text())


        if result.count() > 1:
            self.list_of_all_reports.show_tickets_info(result)
            self.list_of_all_reports.show()


        else:
            self.ticket_info.show_ticket_info(result)
            self.ticket_info.show()


if __name__ == '__main__':
    app = QApplication([])
    print("hi")
    app.setApplicationName("cut_the_line")
    window = search_ticket()
    window.show()

    app.exec_()
