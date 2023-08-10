from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import sys
import os
from NTF import Ui
import shutil


class Dlg(QDialog, Ui):
    def __init__(self):
        super(Dlg, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.clear)
        self.pushButton_2.clicked.connect(self.openfile)
        self.pushButton_3.clicked.connect(self.out1)
        self.pushButton_4.clicked.connect(self.out2)
        self.lineEdit_3.setText("无")

    def out1(self):
        global fn, name, workspace
        last_name = ''
        find = False
        item = []
        item.append(self.comboBox.currentText())
        item.append(self.comboBox_2.currentText())
        item.append(self.comboBox_3.currentText())
        item.append(self.comboBox_4.currentText())
        item.append(self.comboBox_5.currentText())
        item.append(self.lineEdit_3.text())
        for i in item:
            tmp = i
            if not tmp == "无":
                if find:
                    QMessageBox.critical(self, "Error", "检测到多个指定格式，请选择一个，其余的设为无")
                    return 0
                last_name = tmp
                find = True
        if not find:
            QMessageBox.critical(self, "Error", "没有检测到指定格式，请选择一个")
            return 0
        os.chdir(workspace)
        path, tmpname = os.path.split(fn)
        if path == workspace:
            QMessageBox.critical(self, "Error", "转换文件和目标文件夹不可以在同一目录，否则会造成原文件丢失")
            return 0
        shutil.copy(fn, workspace)
        shutil.move(tmpname, self.lineEdit_2.text()+last_name)
        QMessageBox.information(self, "Info", "成功转换!")

    def out2(self):
        f = QFileDialog.getExistingDirectory(self, "选择文件夹", '')
        global fn, name, workspace
        last_name = ''
        find = False
        item = []
        item.append(self.comboBox.currentText())
        item.append(self.comboBox_2.currentText())
        item.append(self.comboBox_3.currentText())
        item.append(self.comboBox_4.currentText())
        item.append(self.comboBox_5.currentText())
        item.append(self.lineEdit_3.text())
        for i in item:
            tmp = i
            if not tmp == "无":
                if find:
                    QMessageBox.critical(self, "Error", "检测到多个指定格式，请选择一个，其余的设为无")
                    return 0
                last_name = tmp
                find = True
        if not find:
            QMessageBox.critical(self, "Error", "没有检测到指定格式，请选择一个")
            return 0
        os.chdir(f)
        path, tmpname = os.path.split(fn)
        if path == f:
            QMessageBox.critical(self, "Error", "转换文件和目标文件夹不可以在同一目录，否则会造成原文件丢失")
            return 0
        shutil.copy(fn, f)
        shutil.move(tmpname, self.lineEdit_2.text()+last_name)
        QMessageBox.information(self, "Info", "成功转换!")

    def clear(self):
        self.lineEdit.clear()

    def openfile(self):
        global fn, name
        fn, name = QFileDialog.getOpenFileName(self, '', '', '所有文件(*.*)')
        self.lineEdit.setText(fn)


if __name__ == "__main__":
    fn = ''
    name = ''
    workspace = r"C:\NTF"
    if os.path.exists(workspace):
        pass
    else:
        os.mkdir(workspace)
    app = QApplication(sys.argv)
    win = Dlg()
    win.setWindowIcon(QIcon("ico.ico"))
    win.show()
    sys.exit(app.exec_())
