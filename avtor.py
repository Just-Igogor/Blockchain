# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget
from mainChain import API_RentalPlatform
from auth_manager import AuthManager
import sys
from admin import Ui_Form3
from Base import Ui_MainWindow_Base


class Ui_MainWindow_Avtor(QWidget):
    def __init__(self):
        super().__init__()
        self.api = API_RentalPlatform()
        self.auth_manager = AuthManager()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setWindowOpacity(3.0)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 40, 801, 80))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(75, 200, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 150, 401, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(400, 150, 401, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.label_3.setObjectName("label_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(399, 170, 3, 329))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.line.setFont(font)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setObjectName("line")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(75, 260, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(75, 320, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(75, 380, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(475, 200, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(475, 260, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(75, 450, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(475, 330, 250, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.handle_registration)
        self.pushButton_2.clicked.connect(self.handle_login)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "BlockLease"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "ETH адресс"))
        self.label_2.setText(_translate("MainWindow", "Регистрация"))
        self.label_3.setText(_translate("MainWindow", "Вход"))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.lineEdit_3.setPlaceholderText(_translate("MainWindow", "ФИО"))
        self.lineEdit_4.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.lineEdit_5.setPlaceholderText(_translate("MainWindow", "Логин"))
        self.lineEdit_6.setPlaceholderText(_translate("MainWindow", "Пароль"))
        self.pushButton.setText(_translate("MainWindow", "Зарегистрироваться"))
        self.pushButton_2.setText(_translate("MainWindow", "Вход"))

    def handle_registration(self):
        login = self.lineEdit_2.text()
        password = self.lineEdit_4.text()
        eth_address = self.lineEdit.text()

        if not login or not password or not eth_address:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Все поля должны быть заполнены.")
            return

        try:
            self.auth_manager.add_user(login, password, eth_address)
            QtWidgets.QMessageBox.information(None, "Успех", "Регистрация прошла успешно.")
            self.lineEdit_2.setText("")
            self.lineEdit_4.setText("")
            self.lineEdit.setText("")
        except ValueError as e:
            QtWidgets.QMessageBox.warning(None, "Ошибка", str(e))

    def handle_login(self):
        login = self.lineEdit_5.text()
        password = self.lineEdit_6.text()

        eth_address = self.auth_manager.validate_user(login, password)
        if eth_address:
            try:
                self.api.unlock_account(eth_address, password)
                QtWidgets.QMessageBox.information(None, "Успех", f"Вы вошли в систему как {login}.")
                
                self.lineEdit_5.setText("")
                self.lineEdit_6.setText("")

                self.base_window = QtWidgets.QMainWindow()
                self.ui_base = Ui_MainWindow_Base()
                self.ui_base.setupUi(self.base_window)
                self.base_window.show()
            except Exception as e:
                QtWidgets.QMessageBox.warning(None, "Ошибка", f"Не удалось разблокировать аккаунт: {str(e)}")
        else:
            QtWidgets.QMessageBox.warning(None, "Ошибка", "Неверный логин или пароль.")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_Avtor()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
