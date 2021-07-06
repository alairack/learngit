# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ip_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys


class Ui_ip_window(object):
    def setupUi(self, ip_window):
        ip_window.setObjectName("ip_window")
        ip_window.resize(492, 347)
        ip_window.setMaximumSize(QtCore.QSize(560, 347))
        ip_window.setStyleSheet("#ip_window{background-color:white}")
        ip_window.setWindowIcon((QtGui.QIcon("image/weather_log.ico")))
        self.centralWidget = QtWidgets.QWidget(ip_window)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(78, 50, 241, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_3.setMinimumWidth(156)
        self.horizontalLayout.addWidget(self.label_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(90, 10, 221, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 91, 71))
        font = QtGui.QFont()
        font.setFamily("仿宋")
        font.setPointSize(18)
        font.setBold(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralWidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(190, 110, 231, 151))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setMinimumWidth(249)
        self.label_6.setGeometry(QtCore.QRect(10, 210, 221, 45))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setMinimumWidth(239)
        self.verticalLayout.addWidget(self.label_7)
        self.label_8 = QtWidgets.QLabel(self.centralWidget)
        self.label_8.setObjectName("label_8")
        self.label_8.setGeometry(QtCore.QRect(72, 190, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setText("")
        ip_window.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(ip_window)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 344, 23))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName('menu')
        self.menu.setTitle("历史记录")
        ip_window.setMenuBar(self.menuBar)
        self.menuBar.addAction(self.menu.menuAction())
        self.menu_2 = QtWidgets.QMenu(self.menu)
        self.menu_2.setObjectName('menu_2')
        self.menu_2.setTitle('选择历史记录')
        self.menu.addMenu(self.menu_2)
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName('menu3')
        self.menu_3.setTitle("选择城市")
        self.menuBar.addMenu(self.menu_3)
        self.menu_4 = QtWidgets.QAction(ip_window)
        self.menu_4.setObjectName('menu_4')
        self.menu_4.setText("设置存储历史记录条数")
        self.menu_4.setEnabled(True)
        self.menu.addAction(self.menu_4)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralWidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 85, 261, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.label_9.setMinimumWidth(180)
        self.horizontalLayout_3.addWidget(self.label_9)
        self.label_10 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName("label_3")
        self.label_10.setMinimumWidth(140)
        self.clear_history = QtWidgets.QAction(ip_window)
        self.clear_history.setEnabled(True)
        self.clear_history.setObjectName('clear_history')
        self.clear_history.setText("清除历史记录")
        self.horizontalLayout_3.addWidget(self.label_10)
        self.statusBar = QtWidgets.QStatusBar(ip_window)
        self.statusBar.setObjectName("statusBar")
        ip_window.setStatusBar(self.statusBar)
        self.retranslateUi(ip_window)
        QtCore.QMetaObject.connectSlotsByName(ip_window)

    def error_window(self):
        QMessageBox.critical(None, 'ERROR', '不是国内ip')
        sys.exit(0)

    def error_window2(self):
        QMessageBox.critical(None, "ERROR", "读取城市列表失败，请检查文件")
        sys.exit(0)

    def error_window3(self):
        QMessageBox.critical(None, 'ERROR', '读取历史记录失败！')



    def retranslateUi(self, ip_window):
        _translate = QtCore.QCoreApplication.translate
        ip_window.setWindowTitle(_translate("ip_window", "天气查询结果"))
        self.label_2.setText(_translate("ip_window", "您所在城市："))
        self.label.setText(_translate("ip_window", "您的ip为："))
        self.label_4.setText(_translate("ip_window", ""))
        self.label_5.setText(_translate("ip_window", ""))
        self.label_6.setText(_translate("ip_window", ""))
        self.label_9.setText(_translate('ip_window', "您当前查询城市:"))
        self.label_10.setText(_translate("ip_window", ""))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ip_window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
