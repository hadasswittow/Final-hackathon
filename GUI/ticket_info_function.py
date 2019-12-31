from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from ticket_info import Ui_MainWindow
from dbquerey import set_status_to_appealed
from dbquerey import set_status_to_non_appealed


class ticket_info(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ticket_info, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.pushButton_accept.setVisible(False)
        self.pushButton_deny.setVisible(False)
        self.pushButton_accept.clicked.connect(self.change_to_appealed)
        self.pushButton_deny.clicked.connect(self.change_to_non_appealed)

    def show_ticket_info_list(self, info: list):
        self.lineEdit_license_plate.setText(info[1])
        self.lineEdit_location.setText(info[5])
        self.lineEdit_report_number.setText(str(info[0]))
        self.lineEdit_time.setText(info[3])
        pix = QPixmap(info[4])
        self.label_3.setPixmap(pix.scaled(self.label_3.width(), self.label_3.height(), QtCore.Qt.KeepAspectRatio,
                                          QtCore.Qt.SmoothTransformation))
        if info[6] == "sent":
            self.pushButton_accept.setVisible(True)
            self.pushButton_deny.setVisible(True)

    def show_ticket_info(self, info):
        self.lineEdit_license_plate.setText(info[0]['license_number'])
        self.lineEdit_location.setText(info[0]['area'])
        self.lineEdit_report_number.setText(str(info[0]['_id']))
        self.lineEdit_time.setText(info[0]['time'])
        pix = QPixmap(info[0]['image'])
        self.label_3.setPixmap(pix.scaled(self.label_3.width(), self.label_3.height(), QtCore.Qt.KeepAspectRatio,
                                          QtCore.Qt.SmoothTransformation))
        if info[0]['status'] == "sent":
            self.pushButton_accept.setVisible(True)
            self.pushButton_deny.setVisible(True)

    def change_to_appealed(self):
        set_status_to_appealed()
        self.pushButton_accept.setVisible(False)
        self.pushButton_deny.setVisible(False)

    def change_to_non_appealed(self):
        set_status_to_non_appealed()
        self.pushButton_accept.setVisible(False)
        self.pushButton_deny.setVisible(False)


if __name__ == '__main__':
    app = QApplication([])
    print("hi")
    app.setApplicationName("cut_the_line")
    window = ticket_info()
    window.show()

    app.exec_()
