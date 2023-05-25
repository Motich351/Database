from database import global_init, create_session
import sys

from PyQt5.QtWidgets import QMainWindow

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
        self.pushButton.clicked.connect(self.load_table)
        self.tableWidget.doubleClicked.connect(self.update_student)