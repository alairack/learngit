import json
import ip_window
from PyQt5.QtWidgets import QAction,  QInputDialog
from PyQt5 import QtCore
import connect
import ctypes
import pickle
from functools import partial
from update import *
import sys
import shutil
import webbrowser


def setting_history(info):
    """
    此函数获得设置的历史记录条数和已存在的历史记录条数，并判断是否储存
    """
    def get_history_number():
        try:
            with open('history.pkl', 'rb') as f1:
                y = pickle.load(f1)
                save_number = len(y)
            return save_number
        except FileNotFoundError:
            f = open('history.pkl', 'wb')
            pickle.dump({}, f)
            f.close()
            history_number = get_history_number()
            return history_number
        except EOFError:
            f = open('history.pkl', 'wb')
            pickle.dump({}, f)
            f.close()
            history_number = get_history_number()
            return history_number
        except TypeError:
            f = open('history.pkl', 'wb')
            pickle.dump({}, f)
            f.close()
            history_number = get_history_number()
            return history_number
        except:
            f = open('history.pkl', 'wb')
            pickle.dump({}, f)
            f.close()
            history_number = get_history_number()
            return history_number
    exist_number = get_history_number()
    setting_number = get_history_settings(info)
    if exist_number >= setting_number:
        return setting_number
    else:
        connect.save_history(info)
        return setting_number


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
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", f"{date}  历史天气"))


def read_history(self):
    """
    read_history函数用于读取已有的历史记录,在54行的connect需只能连接函数本身（函数后不能加括号）
    h变量指向在 “选择历史记录”下创建的历史记录（action)
    """
    try:
        f = open('history.pkl', 'rb')
        content = pickle.load(f)
        f.close()
        if type(content) == dict:
            names = self.__dict__
            number = 1
            for date, value in content.items():
                weather = value[3]
                names['history' + str(number)] = QAction(MainWindow)
                names['history' + str(number)].setEnabled(True)
                names['history' + str(number)].setObjectName('history' + str(number))
                names['history' + str(number)].setText(f"{date} {weather[3]}   {weather[1]}   {weather[2]}")
                self.menu_2.addAction(names['history' + str(number)])
                h = names['history' + str(number)]
                h.triggered.connect(partial(show_history, ui, date))
                number = number + 1
    except:
        QMessageBox.critical(None, '错误', '读取历史记录失败！', QMessageBox.Ok)


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
            QMessageBox.critical(None, '错误', '读取城市列表文件错误，请检查package.json!', QMessageBox.Ok)
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
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", f"{city} 查询结果"))
    try:
        show_city()
    except:
        self.error_window2()


def get_history_settings(info):
    """
    此函数获取存在文本文件中的历史记录设置，返回历史记录设置条数
    rfind函数参考自： https://blog.csdn.net/qq_43894151/article/details/113876461
    """
    try:
        with open('config.txt', 'r') as f:
            content = f.read()
            history_number = content[content.rfind("history_number=", 0, 17):][-2:]
            history_number = int(history_number)
        if history_number == -1 and type(history_number) == 'NoneType':
            with open('config.txt', 'w') as f2:
                f2.write("history_number=10")
            history_number = get_history_settings(info)
            return history_number
        else:
            return history_number
    except FileNotFoundError:
        with open('config.txt', 'w') as f1:
            f1.write("history_number=10")
        history_number = get_history_settings(info)
        return history_number
    except:
        with open('config.txt', 'w') as f1:
            f1.write("history_number=10")
        history_number = get_history_settings(info)
        return history_number


def input_history_setting(history_number):
    """
    此函数为历史记录条数输入框，由setting_history调用
    """
    input_number, ok = QInputDialog.getInt(MainWindow, '输入历史记录条数', '请输入最多存储多少条历史记录（最多为99)', history_number, 0, 99, 1)
    if ok:
        input_number = str(input_number)
        s = "history_number=" + input_number
        with open("config.txt", "w") as f:
            f.write(s)


def query_today_weather(self):
    """
    查询当前天气按钮，并判断是否存储
    """
    connect_info = connect.run_main()
    show_weather(self, connect_info)
    setting_history(connect_info)
    _translate = QtCore.QCoreApplication.translate
    MainWindow.setWindowTitle(_translate("MainWindow", "当前天气查询结果"))


def after_update_run():
    os.remove('../update.bat')
    shutil.rmtree('../pyweather_update')    # 递归删除文件夹
    os.remove('../pyweather_update.zip')
    QtWidgets.QMessageBox.information(None, "更新完成", "新版本已更新完毕", QtWidgets.QMessageBox.Ok)


def manual_update():
    value = judge_update()
    if value == 'new':
        QMessageBox.information(None, '检查更新结果', "您使用的是最新版本！", QMessageBox.Ok)
    else:
        pass


def cmd_command():
    info = connect.run_main()
    inner_ip, outer_ip, ip_location = info[0], info[1], info[2]
    weather, lunar = info[3], info[4]
    print(f'你的内部ip为： {inner_ip} ')
    print(f'你的外部ip为:  {outer_ip}')
    print(f'你所在的地区为:  {ip_location}')
    print('-------------------------------------------------------------------------')
    print(f'农历是: {lunar[0]} {lunar[1]} {lunar[2]}')
    print(f'天气为: {weather}')
    print('\n')


def run(self):
    connect_info = connect.run_main()
    show_weather(self, connect_info)
    setting_number = setting_history(connect_info)
    self.menu_4.triggered.connect(partial(input_history_setting, setting_number))
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("184232")  # ctypes方法解决任务栏图标不更改的问题，且提高运行速度
    MainWindow.show()
    read_history(self)
    clear_his(self, MainWindow)
    choose_city(self)
    about(self)
    self.menu_5.triggered.connect(partial(query_today_weather, self))
    self.update.triggered.connect(manual_update)
    if os.path.isfile("../update.bat"):
        after_update_run()
    else:
        judge_update()
    sys.exit(app.exec_())


def about(self):
    def about_dialog():
        content = 'pyweather by alairack\n在哪可以找到我: https://github.com/alairack/pyweather'
        mag = QMessageBox()
        mag.setText(content)
        mag.setWindowTitle('关于')
        mag.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        mag.addButton('用浏览器打开', QMessageBox.YesRole)
        mag.addButton('关闭', QMessageBox.NoRole)
        choose = mag.exec_()
        if choose:
            pass
        else:
            webbrowser.open('https://github.com/alairack/pyweather')
    self.about.triggered.connect(about_dialog)


if __name__ == "__main__":
    try:
        input_city = sys.argv[2]
        city_info = connect.get_weather(input_city)
        print(f'{input_city}: {city_info}')
    except IndexError:
        try:
            if sys.argv[1] == '--cmd':
                cmd_command()
            else:
                app = QApplication(sys.argv)
                MainWindow = QtWidgets.QMainWindow()
                ui = ip_window.Ui_ip_window()
                ui.setupUi(MainWindow)
                run(ui)
        except IndexError:
            app = QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = ip_window.Ui_ip_window()
            ui.setupUi(MainWindow)
            run(ui)
