# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '脑瘫格式工厂.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(865, 605)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 731, 181))
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(20, 60, 461, 41))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(520, 30, 121, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 100, 121, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 30, 131, 16))
        self.label.setObjectName("label")
        self.groupBox_2 = QtWidgets.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(30, 230, 381, 231))
        self.groupBox_2.setObjectName("groupBox_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 40, 113, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 131, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 110, 361, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 160, 361, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.groupBox_3 = QtWidgets.QGroupBox(Form)
        self.groupBox_3.setGeometry(QtCore.QRect(450, 240, 311, 251))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox.setGeometry(QtCore.QRect(170, 30, 87, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setItemText(7, "")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_3)
        self.label_8.setGeometry(QtCore.QRect(10, 70, 101, 16))
        self.label_8.setObjectName("label_8")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 70, 87, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_9 = QtWidgets.QLabel(self.groupBox_3)
        self.label_9.setGeometry(QtCore.QRect(10, 110, 101, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_3.setGeometry(QtCore.QRect(170, 110, 87, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_10 = QtWidgets.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 220, 151, 16))
        self.label_10.setObjectName("label_10")
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_4.setGeometry(QtCore.QRect(170, 180, 87, 22))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(7, "")
        self.label_11 = QtWidgets.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 140, 101, 16))
        self.label_11.setObjectName("label_11")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_5.setGeometry(QtCore.QRect(170, 140, 87, 22))
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.label_12 = QtWidgets.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 180, 101, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(170, 220, 113, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "脑瘫格式工厂"))
        self.groupBox.setTitle(_translate("Form", "文件操作"))
        self.pushButton.setText(_translate("Form", "清空"))
        self.pushButton_2.setText(_translate("Form", "浏览"))
        self.label.setText(_translate("Form", "欲转换的文件："))
        self.groupBox_2.setTitle(_translate("Form", "文件输出"))
        self.label_2.setText(_translate("Form", "文件名(不加格式):"))
        self.pushButton_3.setText(_translate("Form", "默认文件夹输出"))
        self.pushButton_4.setText(_translate("Form", "自定义文件夹输出"))
        self.groupBox_3.setTitle(_translate("Form", "文件格式(仅选择一个，其余设为无)"))
        self.comboBox.setItemText(0, _translate("Form", "无"))
        self.comboBox.setItemText(1, _translate("Form", ".ini"))
        self.comboBox.setItemText(2, _translate("Form", ".log"))
        self.comboBox.setItemText(3, _translate("Form", ".txt"))
        self.comboBox.setItemText(4, _translate("Form", ".java"))
        self.comboBox.setItemText(5, _translate("Form", ".py"))
        self.comboBox.setItemText(6, _translate("Form", ".html"))
        self.label_7.setText(_translate("Form", "文本格式:"))
        self.label_8.setText(_translate("Form", "图片视频格式:"))
        self.comboBox_2.setItemText(0, _translate("Form", "无"))
        self.comboBox_2.setItemText(1, _translate("Form", ".ico"))
        self.comboBox_2.setItemText(2, _translate("Form", ".mp3"))
        self.comboBox_2.setItemText(3, _translate("Form", ".avi"))
        self.comboBox_2.setItemText(4, _translate("Form", ".jpg"))
        self.comboBox_2.setItemText(5, _translate("Form", ".png"))
        self.comboBox_2.setItemText(6, _translate("Form", ".jpeg"))
        self.comboBox_2.setItemText(7, _translate("Form", ".gif"))
        self.label_9.setText(_translate("Form", "音频格式:"))
        self.comboBox_3.setItemText(0, _translate("Form", "无"))
        self.comboBox_3.setItemText(1, _translate("Form", ".mp3"))
        self.comboBox_3.setItemText(2, _translate("Form", ".ogg"))
        self.comboBox_3.setItemText(3, _translate("Form", ".m4a"))
        self.label_10.setText(_translate("Form", "自定义格式(如.xxx):"))
        self.comboBox_4.setItemText(0, _translate("Form", "无"))
        self.comboBox_4.setItemText(1, _translate("Form", ".sys"))
        self.comboBox_4.setItemText(2, _translate("Form", ".db"))
        self.comboBox_4.setItemText(3, _translate("Form", ".exe"))
        self.comboBox_4.setItemText(4, _translate("Form", ".dll"))
        self.comboBox_4.setItemText(5, _translate("Form", ".ink"))
        self.comboBox_4.setItemText(6, _translate("Form", ".url"))
        self.label_11.setText(_translate("Form", "压缩格式:"))
        self.comboBox_5.setItemText(0, _translate("Form", "无"))
        self.comboBox_5.setItemText(1, _translate("Form", ".zip"))
        self.comboBox_5.setItemText(2, _translate("Form", ".7z"))
        self.comboBox_5.setItemText(3, _translate("Form", ".rar"))
        self.comboBox_5.setItemText(4, _translate("Form", ".jar"))
        self.comboBox_5.setItemText(5, _translate("Form", ".iso"))
        self.label_12.setText(_translate("Form", "其他格式:"))
