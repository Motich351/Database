from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog, QMessageBox

from database import global_init, create_session, Shop, Product, ShopProduct
from ui_Product import Ui_ProductAdd
from ui_Shop_ProductTab import Ui_Form


class ShopProductTab(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_is_changeable = True
        self.session = None
        self.sp_adder = None
        self.sp_updater = None
        self.initUI()
        self.load_table()

    def initUI(self):
        global_init("database/db.db")
        self.session = create_session()
        #self.tableShopProduct.doubleClicked.connect(self.update_sp)
        #self.AddShopProduct.clicked.connect(self.add_sp)
        #self.ShopProductUpdate.clicked.connect(self.load_table)
        #self.SearchShopProduct.clicked.connect(self.search_sp)
        #self.DeleteShopProduct.clicked.connect(self.delete_sp)

    def load_table(self):
        self.table_is_changeable = False
        shop_products = self.session.query(ShopProduct).all()
        self.tableShopProduct.setRowCount(0)
        for shop_product in shop_products:
            row_position = self.tableShopProduct.rowCount()
            self.tableShopProduct.insertRow(row_position)
            tmp = QTableWidgetItem(str(shop_product.shop_id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableShopProduct.setItem(row_position, 0, tmp)
            tmp = QTableWidgetItem(str(shop_product.product_id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableShopProduct.setItem(row_position, 1, tmp)

        self.table_is_changeable = True

