from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QMainWindow, QApplication

from ticket_info import Ui_MainWindow


class ticket_info(Ui_MainWindow, QMainWindow):
    def __init__(self, *args, **kwargs):
        super(ticket_info, self).__init__(*args, **kwargs)
        self.setupUi(self)

    def show_ticket_info_list(self, info: list):
        self.lineEdit_license_plate.setText(info[1])
        self.lineEdit_location.setText(info[5])
        self.lineEdit_report_number.setText(str(info[0]))
        self.lineEdit_time.setText(info[3])
        pix = QPixmap(r"C:\Users\RENT\Desktop\untitled\car.jpg")
        self.label_3.setPixmap(pix.scaled(self.label_3.width(), self.label_3.height(), QtCore.Qt.KeepAspectRatio,
                                          QtCore.Qt.SmoothTransformation))

    def show_ticket_info(self, info):
        self.lineEdit_license_plate.setText(info[0]['license_number'])
        self.lineEdit_location.setText(info[0]['area'])
        self.lineEdit_report_number.setText(str(info[0]['_id']))
        self.lineEdit_time.setText(info[0]['time'])
        pix = QPixmap(r"C:\Users\RENT\Desktop\untitled\car.jpg")
        self.label_3.setPixmap(pix.scaled(self.label_3.width(), self.label_3.height(), QtCore.Qt.KeepAspectRatio,
                                          QtCore.Qt.SmoothTransformation))


if __name__ == '__main__':
    app = QApplication([])
    print("hi")
    app.setApplicationName("cut_the_line")
    window = ticket_info()
    window.show()

    app.exec_()
