from PyQt5.QtCore import QModelIndex, Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog, QMessageBox

from database import global_init, create_session, Product
from ui_Product import Ui_ProductAdd
from ui_ProductTab import Ui_Form


class ProductTab(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.table_is_changeable = True
        self.session = None
        self.product_adder = None
        self.product_updater = None
        self.initUI()
        self.load_table()

    def initUI(self):
        global_init("database/db.db")
        self.session = create_session()
        self.tableProduct.doubleClicked.connect(self.update_product)
        self.AddProduct.clicked.connect(self.add_product)
        self.ProductUpdate.clicked.connect(self.load_table)
        self.SearchProduct.clicked.connect(self.search_product)
        self.DeleteProduct.clicked.connect(self.delete_product)

    def load_table(self):
        self.table_is_changeable = False
        products = self.session.query(Product).all()
        self.tableProduct.setRowCount(0)
        for product in products:
            row_position = self.tableProduct.rowCount()
            self.tableProduct.insertRow(row_position)
            tmp = QTableWidgetItem(str(product.id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableProduct.setItem(row_position, 0, tmp)
            tmp = QTableWidgetItem(str(product.name))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableProduct.setItem(row_position, 1, tmp)
            tmp = QTableWidgetItem(str(product.price))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableProduct.setItem(row_position, 2, tmp)
            tmp = QTableWidgetItem(str(product.numb))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableProduct.setItem(row_position, 3, tmp)
            # product_names = ', '.join([shop_product.product.name for shop_product in shop.products])
            # tmp = QTableWidgetItem(product_names)
            # tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            # self.TablePoint.setItem(row_position, 4, tmp)
        self.table_is_changeable = True

    def search_product(self):
        search_text = self.lineProduct.text()
        if not search_text:
            self.load_table()
            return

        products = self.session.query(Product).filter(
            (Product.name.ilike(f"%{search_text}%")) |
            (Product.price.ilike(f"%{search_text}%")) |
            (Product.numb.ilike(f"%{search_text}%"))
        ).all()

        self.tableProduct.setRowCount(0)
        for row, product in enumerate(products):
            self.tableProduct.insertRow(row)
            self.tableProduct.setItem(row, 0, QTableWidgetItem(str(product.id)))
            self.tableProduct.setItem(row, 1, QTableWidgetItem(str(product.name)))
            self.tableProduct.setItem(row, 2, QTableWidgetItem(str(product.price)))
            self.tableProduct.setItem(row, 3, QTableWidgetItem(str(product.numb)))

    def update_product(self, index: QModelIndex):
        current_row = index.row()
        id_ = int(self.tableProduct.item(current_row, 0).text())
        self.product_updater = ProductUpdater(id_)
        self.product_updater.exec_()
        self.load_table()

    def add_product(self):
        self.product_adder = ProductAdder(self.session)
        if self.product_adder.exec_():
            new_product = Product(
                name=self.product_adder.lineProductName.text(),
                price=self.product_adder.lineProductPrice.text(),
                numb=self.product_adder.lineProductCount.text(),
            )
            self.session.add(new_product)
            self.session.commit()
            self.load_table()

    def delete_product(self, delete_by_search=True):
        search_text = self.lineProduct.text().strip()

        if delete_by_search:
            if not search_text:
                pass
        else:
            selected_rows = self.tableProduct.selectionModel().selectedRows()
            if not selected_rows:
                return
            products = [
                self.session.query(Product).get(int(self.tableProduct.item(row.row(), 0).text())) for
                row in
                selected_rows]

        reply = QMessageBox.question(
            self, "Удалить товар", "Вы хотите удалить выбранный(ые) товар(ы)?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.No:
            return  # Deletion canceled
        for product in products:
            self.session.delete(product)
            self.session.commit()

        self.load_table()


class ProductUpdater(QDialog, Ui_ProductAdd):
    def __init__(self, product_id):
        super().__init__()
        self.setupUi(self)

        self.session = create_session()
        self.product = self.session.query(Product).get(product_id)
        self.idProduct.setText(str(self.product.id))
        self.lineProductName.setText(str(self.product.name))
        self.lineProductPrice.setText(str(self.product.price))
        self.lineProductCount.setText(str(self.product.numb))

        self.SaveProduct.clicked.connect(self.save_data)

    def save_data(self):
        self.product.name = self.lineProductName.text()
        self.product.price = self.lineProductPrice.text()
        self.product.numb = self.lineProductCount.text()
        self.session.commit()
        self.close()


class ProductAdder(QDialog, Ui_ProductAdd):
    def __init__(self, session):
        super().__init__()
        self.setupUi(self)

        self.session = session
        self.product = None
        self.lineProductName.setText("")
        self.lineProductPrice.setText("")
        self.lineProductCount.setText("")

        self.SaveProduct.clicked.connect(self.save_data)

    def save_data(self):
        self.product = Product(
            name=self.lineProductName.text(),
            price=self.lineProductPrice.text(),
            numb=self.lineProductCount.text(),
        )
        self.accept()