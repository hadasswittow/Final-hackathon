# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ticket_info.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(598, 509)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 10, 521, 351))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 271, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_report_number = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_report_number.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_report_number.setObjectName("lineEdit_report_number")
        self.horizontalLayout_4.addWidget(self.lineEdit_report_number)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label1 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label1.setFont(font)
        self.label1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label1.setAutoFillBackground(True)
        self.label1.setObjectName("label1")
        self.horizontalLayout.addWidget(self.label1)
        self.lineEdit_license_plate = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_license_plate.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_license_plate.setObjectName("lineEdit_license_plate")
        self.horizontalLayout.addWidget(self.lineEdit_license_plate)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.lineEdit_location = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_location.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_location.setObjectName("lineEdit_location")
        self.horizontalLayout_3.addWidget(self.lineEdit_location)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_time = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_time.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_time.setObjectName("lineEdit_time")
        self.horizontalLayout_2.addWidget(self.lineEdit_time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(0, 290, 201, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_accept = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_accept.setFont(font)
        self.pushButton_accept.setObjectName("pushButton_accept")
        self.horizontalLayout_5.addWidget(self.pushButton_accept)
        self.pushButton_deny = QtWidgets.QPushButton(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_deny.setFont(font)
        self.pushButton_deny.setObjectName("pushButton_deny")
        self.horizontalLayout_5.addWidget(self.pushButton_deny)
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(299, 30, 201, 251))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 201, 241))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 598, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "TICKET INFORMATIN"))
        self.label_4.setText(_translate("MainWindow", "REPORT NUMBER"))
        self.label1.setText(_translate("MainWindow", "LICENSE PLATE NUMBER"))
        self.label_2.setText(_translate("MainWindow", "LOCATION"))
        self.label.setText(_translate("MainWindow", "TIME"))
        self.pushButton_accept.setText(_translate("MainWindow", "ACCEPT"))
        self.pushButton_deny.setText(_translate("MainWindow", "DENY"))
        self.groupBox_2.setTitle(_translate("MainWindow", "IMAGE"))
        self.label_3.setText(_translate("MainWindow", "TextLabel"))
