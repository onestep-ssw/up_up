import os
import sys
import threading
import time
from PySide6.QtGui import QTextCursor, QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QMessageBox, QSystemTrayIcon, QMenu)
from plyer import notification

from ui.ui_main_interface import Ui_MainWindow


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


ico_path = resource_path("static/up.ico")


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def closeEvent(self, event):
        # 隐藏窗口
        self.hide()
        # trayIcon.iconShow()
        # 忽略关闭事件
        event.ignore()


class MyThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.condition = False

    def run(self):
        count_down_show(self)


class MySystemTrayIcon(QSystemTrayIcon):

    def __init__(self, qMainWindows):
        super(MySystemTrayIcon, self).__init__()
        # 创建系统托盘图标
        self.setIcon(QIcon(ico_path))
        # 显示系统托盘菜单
        menu = QMenu(qMainWindows)
        restore_action = menu.addAction("主界面")
        quit_action = menu.addAction("退出")
        restore_action.triggered.connect(qMainWindows.showNormal)
        quit_action.triggered.connect(self.quitApplication)
        self.setContextMenu(menu)
        self.iconShow()

    def quitApplication(self):
        # 退出应用程序
        self.hide()
        QApplication.quit()

    def iconShow(self):
        self.show()
        pass


def main_page_show(reason):
    activa = QSystemTrayIcon.ActivationReason
    if reason == activa.Trigger or reason == activa.DoubleClick:
        mainWindow.showNormal()


thread_c = None

app = QApplication(sys.argv)

mainWindow = MainWindow()
mainWindow.setFixedSize(mainWindow.width(), mainWindow.height())
icon = QIcon(ico_path)
mainWindow.setWindowIcon(icon)
ui = mainWindow.ui

trayIcon = MySystemTrayIcon(mainWindow)

trayIcon.activated.connect(main_page_show)


## 确认开始倒计时
def confirm_ed():
    if not hint_text_status():
        return None

    confirm_bu(False)
    time_comboBox_and_hint_radio(False)
    global thread_c
    thread_c = MyThread()
    thread_c.condition = False
    thread_c.start()
    thread_c.is_alive()


def count_down_show(thread_p):
    count_second = int(ui.comboBox.currentText()) * 60
    timer = count_down_compute(count_second)
    ui.lineEdit.setText(timer)
    notifyFlag = False
    while count_second >= 0:
        time.sleep(1)
        if thread_p.condition:
            break
        count_second -= 1
        timer = count_down_compute(count_second)
        ui.lineEdit.setText(timer)
        if count_second == 0:
            notifyFlag = True

    ui.lineEdit.setText("00:00")
    if notifyFlag:
        # 通知
        notify_action()

    confirm_bu(True)
    time_comboBox_and_hint_radio(True)
    if thread_p.condition:
        return
    if ui.radioBu_open.isChecked():
        confirm_ed()


def count_down_compute(count_second):
    mins, secs = divmod(count_second, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    return timer


def close_count_down():
    global thread_c
    if thread_c is not None:
        thread_c.condition = True


def remake_count_down():
    global thread_c
    if thread_c is None:
        confirm_ed()
    else:
        close_count_down()
        while thread_c.is_alive():
            pass
        if not thread_c.is_alive():
            confirm_ed()


def confirm_bu(flag):
    ui.confirm_button.setEnabled(flag)


def time_comboBox_and_hint_radio(flag):
    ui.comboBox.setEnabled(flag)
    ui.comboBox_2.setEnabled(flag)
    ui.hint_pt.setEnabled(flag)
    ui.radioBu_open.setEnabled(flag)
    ui.radioBu_close.setEnabled(flag)


def hint_text_limit():
    text_hint = ui.hint_pt.toPlainText()
    text_len = len(text_hint)
    if text_len > 20:
        ui.hint_pt.setPlainText(text_hint[:20])
        text_cursor = ui.hint_pt.textCursor()
        text_cursor.movePosition(QTextCursor.EndOfBlock)
        ui.hint_pt.setTextCursor(text_cursor)


def other_handler():
    ui.confirm_button.clicked.connect(confirm_ed)
    ui.close_button.clicked.connect(close_count_down)
    ui.remake_button.clicked.connect(remake_count_down)

    ui.hint_pt.setPlainText("站起来走一走活动下筋骨")
    ui.hint_pt.textChanged.connect(hint_text_limit)


def notify_action():
    notify_num = int(ui.comboBox_2.currentText())
    for i in range(0, notify_num):
        notification.notify(
            title='起来走走', message=ui.hint_pt.toPlainText(), app_icon=ico_path,
            timeout=3, ticker='', toast=False,)


def loop_open_flag():
    return ui.radioBu_open.isChecked()


def hint_text_status():
    len_t = len(ui.hint_pt.toPlainText())
    if len_t == 0:
        msgBox = QMessageBox()
        msgBox.setWindowTitle("提示")
        msgBox.setText("提示语不能为空")
        msgBox.exec_()
        return False
    return True


def main():
    other_handler()
    mainWindow.show()
    sys.exit(app.exec())
