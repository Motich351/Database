# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WorkerTab.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(758, 474)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.WorkerLine = QtWidgets.QLineEdit(Form)
        self.WorkerLine.setObjectName("WorkerLine")
        self.horizontalLayout_7.addWidget(self.WorkerLine)
        self.SearchWorker = QtWidgets.QPushButton(Form)
        self.SearchWorker.setObjectName("SearchWorker")
        self.horizontalLayout_7.addWidget(self.SearchWorker)
        self.verticalLayout_3.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.tableWorker = QtWidgets.QTableWidget(Form)
        self.tableWorker.setObjectName("tableWorker")
        self.tableWorker.setColumnCount(7)
        self.tableWorker.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWorker.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWorker.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWorker.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWorker.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWorker.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWorker.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWorker.setHorizontalHeaderItem(6, item)
        self.horizontalLayout_8.addWidget(self.tableWorker)
        self.verticalScrollBar = QtWidgets.QScrollBar(Form)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.horizontalLayout_8.addWidget(self.verticalScrollBar)
        self.verticalLayout_3.addLayout(self.horizontalLayout_8)
        self.WorkerUpdate = QtWidgets.QPushButton(Form)
        self.WorkerUpdate.setObjectName("WorkerUpdate")
        self.verticalLayout_3.addWidget(self.WorkerUpdate)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.AddWorker = QtWidgets.QPushButton(Form)
        self.AddWorker.setObjectName("AddWorker")
        self.horizontalLayout_12.addWidget(self.AddWorker)
        self.ChangeWorker = QtWidgets.QPushButton(Form)
        self.ChangeWorker.setObjectName("ChangeWorker")
        self.horizontalLayout_12.addWidget(self.ChangeWorker)
        self.horizontalLayout_11.addLayout(self.horizontalLayout_12)
        spacerItem = QtWidgets.QSpacerItem(238, 18, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_10)
        self.DeleteWorker = QtWidgets.QPushButton(Form)
        self.DeleteWorker.setObjectName("DeleteWorker")
        self.horizontalLayout_9.addWidget(self.DeleteWorker)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_13.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.SearchWorker.setText(_translate("Form", "Поиск"))
        item = self.tableWorker.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWorker.horizontalHeaderItem(1)
        item.setText(_translate("Form", "ФИО"))
        item = self.tableWorker.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Должность"))
        item = self.tableWorker.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Телефон"))
        item = self.tableWorker.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Зарплата"))
        item = self.tableWorker.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Пасспорт"))
        item = self.tableWorker.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Адрес"))
        self.WorkerUpdate.setText(_translate("Form", "Обновить данные"))
        self.AddWorker.setText(_translate("Form", "Добавить"))
        self.ChangeWorker.setText(_translate("Form", "Изменить"))
        self.DeleteWorker.setText(_translate("Form", "Удалить"))
