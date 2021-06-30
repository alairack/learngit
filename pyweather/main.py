import ip_window
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import connect
import ctypes


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.child = ip_window.Ui_ip_window()
        self.child.setupUi(self)

    def check_weather(self):
        inner_ip, outer_ip, ip_location, weather, lunar = connect.run_main()
        self.child.lineEdit.setText(outer_ip)
        self.child.label_3.setText(f"{ip_location[0]},{ip_location[1]},{ip_location[2]}")
        self.child.label_4.setText(weather[3])
        self.child.label_5.setText(f'{lunar[3]}月{weather[0]}')
        self.child.label_6.setText(f"{weather[1]} {weather[2]}")
        self.child.label_7.setText(f"{lunar[0]},{lunar[1]}月,{lunar[2]}日")
        self.child.label_8.setText(weather[4])


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.check_weather()
    # 下面的ctypes方法解决任务栏图标不更改的问题，且提高运行速度
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("184232")
    window.show()
    sys.exit(app.exec_())
