import json
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
    self.label_10.setText(ip_location[2])


def show_history(self, date):
    """
    show_history把读取的历史记录传递给show_weather进行显示
    """
    f = open('history.pkl', 'rb')
    content = pickle.load(f)
    f.close()
    date = str(date)
    info = content[date]
    show_weather(self, info)


def read_history(self):
    """
    read_history函数用于读取已有的历史记录,在54行的connect需只能连接函数本身（函数后不能加括号）
    h变量指向在 “选择历史记录”下创建的历史记录（action)
    """
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
        raise ValueError('')


def clear_his(self, window):
    """
    clear_his 执行清除历史记录的相关程序
    """
    def clear():
        f = open('history.pkl', 'wb')
        pickle.dump('', f)
        f.close()

        def set_menu_disable():
            """
            把所有的历史记录action设置为不可点击，如点击会报错
            """
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
    self.menu.addAction(self.clear_history)
    self.clear_history.triggered.connect(clear)


def choose_city(self):
    def show_city():
        try:
            f = open('package.json', encoding='utf-8')
            content = f.read()
        except:
            raise FileNotFoundError("")
        else:
            content = json.loads(content)
            content = content['provinces']
            names = self.__dict__
            number = 1
            for city in content:
                city_list = city['citys']
                names['provinces' + str(number)] = QtWidgets.QMenu(self.menu_3)
                names['provinces' + str(number)].setObjectName('provinces' + str(number))
                names['provinces' + str(number)].setTitle(city['provinceName'])
                self.menu_3.addMenu(names['provinces' + str(number)])
                for city_name in city_list:
                    s = city_name["citysName"]
                    names['city' + str(number)] = QtWidgets.QAction(MainWindow)
                    names['city' + str(number)].setEnabled(True)
                    names['city' + str(number)].setObjectName('city' + str(number))
                    names['city' + str(number)].setText(s)
                    names['provinces' + str(number)].addAction(names['city' + str(number)])
                    h = names['city' + str(number)]
                    h.triggered.connect(partial(run_choose, s))

    def run_choose(city):
        weather = connect.get_weather(city)
        self.label_4.setText(weather[3])
        self.label_6.setText(f"{weather[1]} {weather[2]}")
        self.label_8.setText(weather[4])
        self.label_10.setText(city)
    show_city()


def run(self):
    try:
        weather = check_weather()
        show_weather(self, weather)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("184232")  # ctypes方法解决任务栏图标不更改的问题，且提高运行速度
        MainWindow.show()
        read_history(self)
        clear_his(self, MainWindow)
        choose_city(self)

    except ValueError:
        self.error_window3()
        sys.exit(0)
    except FileNotFoundError:
        self.error_window2()
        sys.exit(0)
    except:
        self.error_window()
        sys.exit(app.exec_())
    else:
        sys.exit(app.exec_())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = ip_window.Ui_ip_window()
    ui.setupUi(MainWindow)
    run(ui)
