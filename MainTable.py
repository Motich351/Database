from sqlalchemy import or_

from database.base_meta import global_init, create_session
from database.worker import Worker
from database.shop import Shop
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTableWidgetItem, QFileDialog, \
    QInputDialog, QColorDialog, QDialog, QMessageBox

from ui_Worker import Ui_WorkerAdd
from ui_Product import Ui_ProductAdd
from ui_Client import Ui_ClientAdd
from ui_table import Ui_MainWindow

from PyQt5.QtCore import Qt, QModelIndex



class TableViewer(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()
        self.table_is_changeable = True

    def initUI(self):
        global_init("database/db.db")
        self.session = create_session()
        self.WorkerUpdate.clicked.connect(self.load_table)
        self.tableWorker.doubleClicked.connect(self.update_worker)
        self.AddWorker.clicked.connect(self.add_worker)
        self.SearchWorker.clicked.connect(self.search_worker)
        self.DeleteWorker.clicked.connect(self.delete_worker)

    def add_worker(self):
        self.worker_adder = WorkerAdder(self.session)
        if self.worker_adder.exec_():
            new_worker = Worker(
                fullname=self.worker_adder.lineFIOWorker.text(),
                jobrank=self.worker_adder.ChooseRankWorker.currentText(),
                phone=self.worker_adder.linePassportWorker_2.text(),
                salary=self.worker_adder.lineSalaryWorker.text(),
                passport=self.worker_adder.linePassportWorker.text(),
                shop_id=self.worker_adder.ChooseWorkerPoint.currentData(),
            )
            self.session.add(new_worker)
            self.session.commit()
            self.load_table()

    def update_worker(self, index: QModelIndex):
        current_row = index.row()
        id_ = int(self.tableWorker.item(current_row, 0).text())
        self.worker_updater = WorkerUpdater(id_)
        self.worker_updater.exec_()
        self.load_table()

    def load_table(self):
        self.table_is_changeable = False
        workers = self.session.query(Worker).all()
        self.tableWorker.setRowCount(0)
        for worker in workers:
            row_position = self.tableWorker.rowCount()
            self.tableWorker.insertRow(row_position)
            tmp = QTableWidgetItem(str(worker.id))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWorker.setItem(row_position, 0, tmp)
            tmp = QTableWidgetItem(str(worker.fullname))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWorker.setItem(row_position, 1, tmp)
            tmp = QTableWidgetItem(str(worker.jobrank))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWorker.setItem(row_position, 2, tmp)
            tmp = QTableWidgetItem(str(worker.phone))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWorker.setItem(row_position, 3, tmp)
            tmp = QTableWidgetItem(str(worker.salary))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWorker.setItem(row_position, 4, tmp)
            tmp = QTableWidgetItem(str(worker.passport))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWorker.setItem(row_position, 5, tmp)
            tmp = QTableWidgetItem(str(worker.shop.address))
            tmp.setFlags(tmp.flags() & ~Qt.ItemIsEditable)
            self.tableWorker.setItem(row_position, 6, tmp)
        self.table_is_changeable = True

    def cell_changed(self, row, col):
        if self.table_is_changeable:
            id_ = int(self.tableWidget.item(row, 0).text())
            worker = self.session.query(Worker). \
                filter(Worker.id == id_).first()
            if col == 1:
                worker.fullname = self.tableWidget.item(row, col).text()
                self.session.commit()
            elif col == 2:
                worker.jobramk = self.tableWidget.item(row, col).text()
                self.session.commit()
            elif col == 3:
                worker.phone = self.tableWidget.item(row, col).text()
                self.session.commit()
            elif col == 4:
                worker.salary = self.tableWidget.item(row, col).text()
                self.session.commit()
            elif col == 5:
                worker.passport = self.tableWidget.item(row, col).text()
                self.session.commit()

    def search_worker(self):
        search_text = self.WorkerLine.text()
        if not search_text:
            self.load_table()  # Display all workers if search input is empty
            return

        workers = self.session.query(Worker).filter(
            (Worker.fullname.ilike(f"%{search_text}%")) |
            (Worker.phone.ilike(f"%{search_text}%")) |
            (Worker.passport.ilike(f"%{search_text}%")) |
            (Worker.jobrank.ilike(f"%{search_text}%")) |
            (Worker.salary.ilike(f"%{search_text}%")) |
            (Shop.address.ilike(f"%{search_text}%"))
        ).all()

        self.tableWorker.setRowCount(0)
        for row, worker in enumerate(workers):
            self.tableWorker.insertRow(row)
            self.tableWorker.setItem(row, 0, QTableWidgetItem(str(worker.id)))
            self.tableWorker.setItem(row, 1, QTableWidgetItem(worker.fullname))
            self.tableWorker.setItem(row, 2, QTableWidgetItem(worker.jobrank))
            self.tableWorker.setItem(row, 3, QTableWidgetItem(str(worker.phone)))
            self.tableWorker.setItem(row, 4, QTableWidgetItem(str(worker.salary)))
            self.tableWorker.setItem(row, 5, QTableWidgetItem(str(worker.passport)))
            self.tableWorker.setItem(row, 6, QTableWidgetItem(str(worker.shop.address)))

    def delete_worker(self, delete_by_search=True):
        search_text = self.WorkerLine.text().strip()

        if delete_by_search:
            if not search_text:
                return  # Empty search text, do nothing

            # Retrieve workers matching the search criteria
            workers = self.session.query(Worker).filter(
                or_(
                    Worker.fullname.ilike(f'%{search_text}%'),
                    Worker.phone.ilike(f'%{search_text}%'),
                    Worker.passport.ilike(f'%{search_text}%'),
                    Worker.jobrank.ilike(f'%{search_text}%'),
                    Worker.salary.ilike(f'%{search_text}%'),
                    Worker.shop.has(Shop.address.ilike(f'%{search_text}%'))
                )
            ).all()
        else:
            selected_rows = self.tableWorker.selectionModel().selectedRows()
            if not selected_rows:
                return  # No rows selected, do nothing

            # Retrieve workers from the selected rows
            workers = [self.session.query(Worker).get(int(self.tableWorker.item(row.row(), 0).text())) for row in
                       selected_rows]

        # Confirm deletion
        reply = QMessageBox.question(
            self, "Delete Worker", "Are you sure you want to delete the selected worker(s)?",
            QMessageBox.Yes | QMessageBox.No
        )
        if reply == QMessageBox.No:
            return  # Deletion canceled

        # Delete the workers from the database
        for worker in workers:
            self.session.delete(worker)
            self.session.commit()

        self.load_table()  # Update the table after deletion


class WorkerUpdater(QDialog, Ui_WorkerAdd):
    def __init__(self, worker_id):
        super().__init__()
        self.setupUi(self)

        self.session = create_session()
        self.worker = self.session.query(Worker).get(worker_id)
        self.label_2.setText(str(self.worker.id))
        self.lineFIOWorker.setText(str(self.worker.fullname))
        self.WorkerRanks = ['Админ','Уборщик','Начальник']
        for WorkerRank in self.WorkerRanks:
            self.ChooseRankWorker.addItem(WorkerRank)
        self.linePassportWorker_2.setText(str(self.worker.phone))
        self.lineSalaryWorker.setText(str(self.worker.salary))
        self.linePassportWorker.setText(str(self.worker.passport))
        shops = self.session.query(Shop).filter(Shop.id != self.worker.shop_id).all()
        self.ChooseWorkerPoint.addItem(self.worker.shop.address, self.worker.shop.id)
        for shop in shops:
            self.ChooseWorkerPoint.addItem(shop.address, shop.id)

        self.SaveWorker.clicked.connect(self.save_data)


    def save_data(self):
        self.worker.fullname = self.lineFIOWorker.text()
        cb = self.ChooseRankWorker.currentText()
        self.worker.jobrank = cb
        self.worker.phone = self.linePassportWorker_2.text()
        self.worker.salary = self.lineSalaryWorker.text()
        self.worker.passport = self.linePassportWorker.text()
        self.worker.passport = self.linePassportWorker.text()
        cb_ci = self.ChooseWorkerPoint.currentIndex()
        shop_id = self.ChooseWorkerPoint.itemData(cb_ci)
        self.worker.shop_id = shop_id
        self.session.commit()
        self.close()


class WorkerAdder(QDialog, Ui_WorkerAdd):
    def __init__(self, session):
        super().__init__()
        self.setupUi(self)

        self.session = session
        self.worker = None
        self.lineFIOWorker.setText("")
        self.linePassportWorker_2.setText("")
        self.lineSalaryWorker.setText("")
        self.linePassportWorker.setText("")

        self.ChooseRankWorker.addItems(['Админ', 'Уборщик', 'Начальник'])
        shops = self.session.query(Shop).all()
        for shop in shops:
            self.ChooseWorkerPoint.addItem(shop.address, shop.id)

        self.SaveWorker.clicked.connect(self.save_data)

    def save_data(self):
        self.worker = Worker(
            fullname=self.lineFIOWorker.text(),
            jobrank=self.ChooseRankWorker.currentText(),
            phone=self.linePassportWorker_2.text(),
            salary=self.lineSalaryWorker.text(),
            passport=self.linePassportWorker.text(),
            shop_id=(self.ChooseWorkerPoint.currentData())
        )
        self.accept()


def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


# Back up the reference to the exceptionhook
sys._excepthook = sys.excepthook

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = TableViewer()
    ex.show()
    sys.exit(app.exec())
