# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Product.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductAdd(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(207, 225)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.idProduct = QtWidgets.QLabel(Dialog)
        self.idProduct.setObjectName("idProduct")
        self.horizontalLayout_4.addWidget(self.idProduct)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.ProductName = QtWidgets.QLabel(Dialog)
        self.ProductName.setObjectName("ProductName")
        self.horizontalLayout_3.addWidget(self.ProductName)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.lineProductName = QtWidgets.QLineEdit(Dialog)
        self.lineProductName.setObjectName("lineProductName")
        self.horizontalLayout_3.addWidget(self.lineProductName)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.ProductPrice = QtWidgets.QLabel(Dialog)
        self.ProductPrice.setObjectName("ProductPrice")
        self.horizontalLayout_2.addWidget(self.ProductPrice)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.lineProductPrice = QtWidgets.QLineEdit(Dialog)
        self.lineProductPrice.setObjectName("lineProductPrice")
        self.horizontalLayout_2.addWidget(self.lineProductPrice)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.ProductCount = QtWidgets.QLabel(Dialog)
        self.ProductCount.setObjectName("ProductCount")
        self.horizontalLayout.addWidget(self.ProductCount)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.lineProductCount = QtWidgets.QLineEdit(Dialog)
        self.lineProductCount.setObjectName("lineProductCount")
        self.horizontalLayout.addWidget(self.lineProductCount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.SaveProduct = QtWidgets.QPushButton(Dialog)
        self.SaveProduct.setObjectName("SaveProduct")
        self.verticalLayout.addWidget(self.SaveProduct)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Изменение товара"))
        self.idProduct.setText(_translate("Dialog", "id "))
        self.ProductName.setText(_translate("Dialog", "Название"))
        self.ProductPrice.setText(_translate("Dialog", "Цена"))
        self.ProductCount.setText(_translate("Dialog", "Количество"))
        self.SaveProduct.setText(_translate("Dialog", "Сохранить"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
