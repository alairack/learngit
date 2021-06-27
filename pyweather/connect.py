import mainwindow
import ip_window
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import main
'''
此文件中部分内容实现主窗口pushbutton的checked信号调出ip查询结果界面
https://blog.csdn.net/weixin_39449466/article/details/81008711
'''


class ParentWindow(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self):
        mainwindow.QtWidgets.QWidget.__init__(self)
        self.main_ui = mainwindow.Ui_MainWindow()
        self.main_ui.setupUi(self)


class ChildWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child = ip_window.Ui_ip_window()
        self.child.setupUi(self)

    def check_weather(self):
        inner_ip, outer_ip, ip_location, weather = main.run_main()
        self.child.lineEdit.setText(outer_ip)
        self.child.label_3.setText(f"{ip_location[0]},{ip_location[1]},{ip_location[2]}")
        self.child.label_4.setText(weather[3])
        self.child.label_5.setText(weather[0])
        self.child.label_6.setText(f"{weather[1]} {weather[2]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ParentWindow()
    child = ChildWindow()
    btn = window.main_ui.pushButton
    child.check_weather()
    btn.clicked.connect(child.show)
    window.show()
    sys.exit(app.exec_())
