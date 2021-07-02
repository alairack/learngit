import ip_window
from PyQt5.QtWidgets import QApplication, QAction, QMessageBox
from PyQt5 import QtWidgets
import sys
import connect
import ctypes
import pickle
from functools import partial


def check_weather():
    connect_info = connect.run_main()
    connect.save_history(connect_info)
    return connect_info


def show_weather(self, info):
    inner_ip, outer_ip, ip_location = info[0], info[1], info[2]
    weather, lunar = info[3], info[4]
    self.lineEdit.setText(outer_ip)
    self.label_3.setText(f"{ip_location[0]},{ip_location[1]},{ip_location[2]}")
    self.label_4.setText(weather[3])
    self.label_5.setText(f'{lunar[3]}月{weather[0]}')
    self.label_6.setText(f"{weather[1]} {weather[2]}")
    self.label_7.setText(f"{lunar[0]},{lunar[1]}{lunar[2]}")
    self.label_8.setText(weather[4])

# show_history把读取的历史记录传递给show_weather显示


def show_history(self, date):
    f = open('history.pkl', 'rb')
    content = pickle.load(f)
    f.close()
    date = str(date)
    info = content[date]
    show_weather(self, info)

# read_history函数用于读取已有的历史记录,在54行的connect需只能连接函数本身（函数后不能加括号）
# h变量指向在 “选择历史记录”下创建的历史记录（action)


def read_history(self):
    f = open('history.pkl', 'rb')
    content = pickle.load(f)
    f.close()
    if type(content) == dict:
        names = self.__dict__
        number = 1
        for date, value in content.items():
            names['history' + str(number)] = QAction(MainWindow)
            names['history' + str(number)].setEnabled(True)
            names['history' + str(number)].setObjectName('history' + str(number))
            names['history' + str(number)].setText(date)
            self.menu_2.addAction(names['history' + str(number)])
            h = names['history' + str(number)]
            h.triggered.connect(partial(show_history, ui, date))
            number = number + 1
    else:
        QMessageBox.critical(None, 'ERROR', '读取历史记录失败！')

# clear_his 执行清除历史记录的相关程序


def clear_his(self, window):
    def clear():
        f = open('history.pkl', 'wb')
        pickle.dump('', f)
        f.close()

        def set_menu_disable():
            names = ui.__dict__
            number = 1
            try:
                while number < 1000:
                    names['history' + str(number)].setEnabled(False)
                    number = number+1
            except:
                pass
        set_menu_disable()
        QMessageBox.information(window, '删除历史记录', '历史记录已删除，重启后生效！')
    self.clear_history = QtWidgets.QAction(window)
    self.clear_history.setEnabled(True)
    self.clear_history.setObjectName('clear_history')
    self.clear_history.setText("清除历史记录")
    self.menu.addAction(self.clear_history)
    self.clear_history.triggered.connect(clear)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ip_window.Ui_ip_window()
    ui.setupUi(MainWindow)
    try:
        show_weather(ui, check_weather())
        # 下面的ctypes方法解决任务栏图标不更改的问题，且提高运行速度
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("184232")
        MainWindow.show()
        read_history(ui)
        clear_his(ui, MainWindow)
    except:
        ui.error_window()
    else:
        sys.exit(app.exec_())
