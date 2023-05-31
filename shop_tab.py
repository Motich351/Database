from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem

from database import global_init, create_session, Shop
from ui_ShopTab import Ui_Form


class ShopTab(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_is_changeable = True
        self.session = None
        self.initUI()
        self.load_table()

    def initUI(self):
        global_init("database/db.db")
        self.session = create_session()

    def load_table(self):
        self.table_is_changeable = False
        shops = self.session.query(Shop).all()
        self.TablePoint.setRowCount(0)
        for shop in shops:
            row_position = self.TablePoint.rowCount()
            self.TablePoint.insertRow(row_position)
            tmp = QTableWidgetItem(str(shop.id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.TablePoint.setItem(row_position, 0, tmp)
            tmp = QTableWidgetItem(str(shop.address))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.TablePoint.setItem(row_position, 1, tmp)
            tmp = QTableWidgetItem(str(shop.income))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.TablePoint.setItem(row_position, 2, tmp)
            tmp = QTableWidgetItem(str(shop.product_id))    #Сделать связь с товаром
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.TablePoint.setItem(row_position, 3, tmp)
            tmp = QTableWidgetItem(str(shop.worker_count_id))   #Сделать связь с работниками
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.TablePoint.setItem(row_position, 4, tmp)
        self.table_is_changeable = True

    
    # def update_worker(self, index: QModelIndex):
    #     current_row = index.row()
    #     id_ = int(self.TablePoint.item(current_row, 0).text())
    #     self.shop_updater = ShopUpdater(id_)    #Добавить класс
    #     self.shop_updater.exec_()
    #     self.load_table()
    
    