from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog, QMessageBox

from sqlalchemy import or_
from database import global_init, create_session, Shop, Product
from ui_Shop import Ui_createShop
from ui_ShopTab import Ui_Form


class ShopTab(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_is_changeable = True
        self.session = None
        self.shop_adder = None
        self.shop_updater = None
        self.initUI()
        self.load_table()

    def initUI(self):
        global_init("database/db.db")
        self.session = create_session()
        self.TablePoint.doubleClicked.connect(self.update_shop)
        self.AddPoint.clicked.connect(self.add_shop)
        self.PointUpdate.clicked.connect(self.load_table)
        self.SearchPoint.clicked.connect(self.search_shop)
        self.DeletePoint.clicked.connect(self.delete_shop)

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
            product_names = ', '.join([shop_product.product.name for shop_product in shop.products])
            tmp = QTableWidgetItem(product_names)
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.TablePoint.setItem(row_position, 3, tmp)
        self.table_is_changeable = True

    def search_shop(self):
        search_text = self.linePoint.text()
        if not search_text:
            self.load_table()
            return

        shops = self.session.query(Shop).join(Shop.products).filter(
            or_(
                Shop.address.ilike(f"%{search_text}%"),
                Shop.income.ilike(f"%{search_text}%"),
                Product.name.ilike(f"%{search_text}%")      #ВОПРОС!
            )
        ).all()

        self.TablePoint.setRowCount(0)
        for row, shop in enumerate(shops):
            self.TablePoint.insertRow(row)
            self.TablePoint.setItem(row, 0, QTableWidgetItem(str(shop.id)))
            self.TablePoint.setItem(row, 1, QTableWidgetItem(shop.address))
            self.TablePoint.setItem(row, 2, QTableWidgetItem(str(shop.income)))
            product_names = ', '.join([shop_product.product.name for shop_product in shop.products])
            self.TablePoint.setItem(row, 3, QTableWidgetItem(product_names))    #ВОПРОС!

    def update_shop(self, index: QModelIndex):
        current_row = index.row()
        id_ = int(self.TablePoint.item(current_row, 0).text())
        self.shop_updater = ShopUpdater(id_)
        self.shop_updater.exec_()
        self.load_table()

    def add_shop(self):
        self.shop_adder = ShopAdder(self.session)
        if self.shop_adder.exec_():
            new_shop = Shop(
                address=self.shop_adder.lineAddShop.text(),
                income=self.shop_adder.ShopIncome_2.text(),
            )
            self.session.add(new_shop)
            self.session.commit()
            self.load_table()

    def delete_shop(self, delete_by_search=True):
        search_text = self.linePoint.text().strip()

        if delete_by_search:
            if not search_text:
                pass
        else:
            selected_rows = self.TablePoint.selectionModel().selectedRows()
            if not selected_rows:
                return
            shops = [
                self.session.query(Shop).get(int(self.TablePoint.item(row.row(), 0).text())) for
                row in
                selected_rows]

        reply = QMessageBox.question(
            self, "Удалить магазин", "Вы хотите удалить выбранный(ые) магазин(ы)?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.No:
            return  # Deletion canceled
        for shop in shops:
            self.session.delete(shop)
            self.session.commit()

        self.load_table()  # Update the table after deletion


class ShopUpdater(QDialog, Ui_createShop):
    def __init__(self, shop_id):
        super().__init__()
        self.setupUi(self)

        self.session = create_session()
        self.shop = self.session.query(Shop).get(shop_id)
        self.labelShop.setText(str(self.shop.id))
        self.lineAddShop.setText(str(self.shop.address))
        self.ShopIncome_2.setText(str(self.shop.income))

        self.pushButton.clicked.connect(self.save_data)

    def save_data(self):
        self.shop.address = self.lineAddShop.text()
        self.shop.income = self.ShopIncome_2.text()
        self.session.commit()
        self.close()


class ShopAdder(QDialog, Ui_createShop):
    def __init__(self, session):
        super().__init__()
        self.setupUi(self)

        self.session = session
        self.shop = None
        self.lineAddShop.setText("")
        self.ShopIncome_2.setText("")

        self.pushButton.clicked.connect(self.save_data)

    def save_data(self):
        self.shop = Shop(
            address=self.lineAddShop.text(),
            income=self.ShopIncome_2.text(),
        )
        self.accept()