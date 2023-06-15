from PyQt5 import QtCore, QtGui, QtWidgets

from product_tab import ProductTab
from shop_product_tab import ShopProductTab
from shop_tab import ShopTab
from worker_tab import WorkerTab

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(814, 521)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWiget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.tabWiget.setFont(font)
        self.tabWiget.setObjectName("tabWiget")
        self.worker = WorkerTab()
        self.worker.setObjectName("worker")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.worker)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.tabWiget.addTab(self.worker, "")
        self.point = ShopTab()
        self.point.setObjectName("point")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.point)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWiget.addTab(self.point, "")
        self.Product = ProductTab()
        self.Product.setObjectName("Product")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.Product)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.tabWiget.addTab(self.Product, "")
        self.shop_product = ShopProductTab()
        self.shop_product.setObjectName("shop_product")
        self.tabWiget.addTab(self.shop_product, "")
        self.verticalLayout.addWidget(self.tabWiget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWiget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWiget.setTabText(self.tabWiget.indexOf(self.worker), _translate("MainWindow", "Работник"))
        self.tabWiget.setTabText(self.tabWiget.indexOf(self.point), _translate("MainWindow", "Точка"))
        self.tabWiget.setTabText(self.tabWiget.indexOf(self.Product), _translate("MainWindow", "Товар"))
        self.tabWiget.setTabText(self.tabWiget.indexOf(self.shop_product), _translate("MainWindow", "Точка-Товар"))
