from sqlalchemy import or_

from database.base_meta import global_init, create_session
from database.worker import Worker
from database.shop import Shop
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QTableWidgetItem, \
    QFileDialog, \
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
        pass
        # global_init("database/db.db")
        # self.session = create_session()

        # self.tableWorker.doubleClicked.connect(self.update_worker)
        # self.WorkerUpdate.clicked.connect(self.load_table)
        # self.AddWorker.clicked.connect(self.add_worker)
        # self.SearchWorker.clicked.connect(self.search_worker)
        # self.DeleteWorker.clicked.connect(self.delete_worker)


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
