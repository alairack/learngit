import shutil
import sys
import requests
import os
import time
import zipfile
import subprocess
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication


def judge_update():
    api = "https://api.github.com/repos/alairack/learngit/releases/latest"
    info = requests.get(api).json()
    update_time = info['published_at']
    path = './pyweather.exe'
    try:
        mtime = os.stat(path).st_mtime
    except FileNotFoundError:
        QMessageBox.warning(None, '警告', '没有找到pyweather.exe文件，无法更新', QMessageBox.Ok)
    else:
        modify_time = time.strftime('%Y-%m-%d %H:%M', time.localtime(mtime))
        update_time = update_time.replace('T', ' ')
        update_time = update_time.replace('Z', '')
        update_time = update_time[:-3]
        exist_file_path = os.path.abspath('.')
        a = update_time[11]
        b = update_time[12]
        c = a + b
        c = int(c)
        c = c + 8  # 获取的时间与北京时间有8个小时的时间差
        c = str(c)
        if len(c) == 1:
            c = '0' + c    # 如果是个位数，就补个零
        update_time = update_time[:11] + c + update_time[13:]
        if update_time > modify_time:
            version = get_version()
            select = QMessageBox.information(None, "有新版本", f"检测到有新版本:{version}, 发布于:{update_time}, 是否更新?", QtWidgets.QMessageBox.Yes)
            if select == QMessageBox.Yes:
                app = QApplication(sys.argv)
                app.quit()
                update_file_path = download(version)
                install(update_file_path, exist_file_path)
        else:
            return 'new'


def get_version():
    api = "https://api.github.com/repos/alairack/learngit/releases/latest"
    info = requests.get(api).json()
    update_version = info["tag_name"]
    return update_version


def download(version):
    link = 'https://github.com/alairack/learngit/releases/download/'
    link = link + version + '/'
    file_name = version.replace('v', 'pyweather')
    link = link + file_name + ".zip"
    zip_path = r'..\pyweather_update.zip'
    unzip_path = r'..\pyweather_update'
    response = requests.get(link)
    with open(zip_path, 'wb') as file:
        file.write(response.content)
        file.flush()
    f = zipfile.ZipFile(zip_path)
    f.extractall(unzip_path)
    f.close()
    update_file_path = unzip_path + r'\pyweather'
    update_file_path = os.path.dirname(os.path.abspath(update_file_path))
    return update_file_path


def install(update_file_path, exist_file_path):
    b = open("../update.bat", 'w')
    templist = "@echo off\n"
    templist = templist + 'taskkill /f /im "pyweather.exe"\n'
    templist = templist + "ping -n 5 127.1>nul\n"   # sleep 4s
    update_file_path = update_file_path + r'\pyweather'
    templist = templist + f"copy {update_file_path} {exist_file_path}\n"
    exe_path = exist_file_path + r'\pyweather.exe'
    templist = templist + f'start {exe_path}\n'
    templist = templist + 'exit'
    b.write(templist)
    b.close()
    path = os.path.abspath('..')
    path = path + '/update.bat'
    subprocess.Popen(path, shell=True)


def install2(update_path, exist_path):
    os.rename(exist_path + r'\pyweather.exe', exist_path + r'\pyweather.exe.temp')
    shutil.copy(update_path, exist_path)
    exe_path = exist_path + r'\pyweather.exe'
    os.execv(exe_path, [exe_path])


if __name__ == "__main__":
    judge_update()
