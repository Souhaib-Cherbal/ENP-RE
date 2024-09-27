import sys
import numpy as np
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
import Admetance_Impedance_calculation
import Login_interface
import RE_UI
import time
from PyQt5.QtGui import QPixmap, QIcon
import SysData
import powerflow
import traceback
import ready_results
import matrices_verifing

from PyQt5 import QtCore, QtGui, QtWidgets


# class Login(QDialog, Login_interface.Ui_Login_Dashboard):
#     def __init__(self):
#         QDialog.__init__(self)
#         self.setupUi(self)
#         icon = QIcon("Resources/ENP Logo.png")
#         self.setWindowIcon(icon)
#         self.pushButton.clicked.connect(self.login_validation)
#     def login_validation(self):
#         if self.username.text() != "ENP" and self.password.text() != "RE":
#             QMessageBox.warning(self, "Error", "Access Denied")
#         else:
#             window1.close()
#             window2.show()

class matrix_verification(QDialog ,matrices_verifing.Ui_admitance_impedance_verification):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)
        icon = QIcon("Resources/ENP Logo.png")
        self.setWindowIcon(icon)
        # ENP_RE()
        # self.verify.clicked.connect(self.checkverification())
    # def checkverification(self):
    #     self.click_verify()

class ENP_RE(QMainWindow, QDialog,RE_UI.Ui_MainWindow,Admetance_Impedance_calculation.calc,powerflow.powerflow, SysData.Data, ready_results.chooseresults):
    def __init__(self):
        super().__init__()
        QDialog.__init__(self)
        self.setupUi(self)
        self.setWindowFlags(self.windowFlags())
        icon = QIcon("Resources/ENP Logo.png")
        self.setWindowIcon(icon)
        pixmap = QPixmap("Resources\shemas\electric_system.png")
        self.system_image.setPixmap(pixmap)
        self.TabWidjet.setCurrentIndex(0)
        self.SysTypeList.setCurrentText("Custom")
        self.SysTypeList.currentIndexChanged.connect(self.systypechose)
        self.Enter.clicked.connect(self.set_tables_rows)
        self.admitance_generate.clicked.connect(self.admitance_generate_clicked)
        self.impedance_generate.clicked.connect(self.impedance_generate_clicked)
        self.powerflow_generate.clicked.connect(self.powerflow_generate_clicked)
        self.save_admitance.clicked.connect(self.save_admitance_results)
        self.Save_impedance.clicked.connect(self.saver_impedance_results)
        self.Save_powerflow.clicked.connect(self.save_powerflow_results)
        self.actionClose.triggered.connect(ENP_RE.close)
        self.actionVirefy_Ybus_Zbus.triggered.connect(window3.show)

    def systypechose(self):
        self.choice = self.SysTypeList.currentText()
        if self.choice == 'Custom':
            pixmap = QPixmap("Resources\shemas\electric_system.png")
            self.system_image.setPixmap(pixmap)
        if self.choice == 'System 3 bus':
            pixmap = QPixmap("Resources\shemas\IEEE3bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("3")
            self.nmb_branches_total.setText("3")
            self.nmb_noeuds_pq.setText("1")
            self.nmb_noeuds_pv.setText("1")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.0001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("0")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 5 bus':
            pixmap = QPixmap("Resources\shemas\IEEE5bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("5")
            self.nmb_branches_total.setText("7")
            self.nmb_noeuds_pq.setText("2")
            self.nmb_noeuds_pv.setText("2")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.0001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("0")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 5 bus cours':
            pixmap = QPixmap("Resources\shemas\IEEE5bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("5")
            self.nmb_branches_total.setText("7")
            self.nmb_noeuds_pq.setText("2")
            self.nmb_noeuds_pv.setText("1")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.0001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("2")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 6 bus':
            pixmap = QPixmap("Resources\shemas\IEEE6bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("6")
            self.nmb_branches_total.setText("7")
            self.nmb_noeuds_pq.setText("3")
            self.nmb_noeuds_pv.setText("2")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.0001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("3")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 9 bus':
            pixmap = QPixmap("Resources\shemas\IEEE9bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("9")
            self.nmb_branches_total.setText("9")
            self.nmb_noeuds_pq.setText("6")
            self.nmb_noeuds_pv.setText("2")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("3")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 10 bus':
            pixmap = QPixmap("Resources\shemas\IEEE10bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("10")
            self.nmb_branches_total.setText("9")
            self.nmb_noeuds_pq.setText("8")
            self.nmb_noeuds_pv.setText("1")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("2")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 11 bus':
            pixmap = QPixmap("Resources\shemas\IEEE11bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("11")
            self.nmb_branches_total.setText("14")
            self.nmb_noeuds_pq.setText("8")
            self.nmb_noeuds_pv.setText("2")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("3")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 14 bus':
            pixmap = QPixmap("Resources\shemas\IEEE14bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("14")
            self.nmb_branches_total.setText("20")
            self.nmb_noeuds_pq.setText("9")
            self.nmb_noeuds_pv.setText("4")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("0")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 26 bus':
            pixmap = QPixmap("Resources\shemas\IEEE26bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("26")
            self.nmb_branches_total.setText("46")
            self.nmb_noeuds_pq.setText("20")
            self.nmb_noeuds_pv.setText("5")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("0")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 30 bus':
            pixmap = QPixmap("Resources\shemas\IEEE30bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("30")
            self.nmb_branches_total.setText("41")
            self.nmb_noeuds_pq.setText("24")
            self.nmb_noeuds_pv.setText("5")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("0")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 47 bus':
            pixmap = QPixmap("Resources\shemas\IEEE47bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("47")
            self.nmb_branches_total.setText("69")
            self.nmb_noeuds_pq.setText("38")
            self.nmb_noeuds_pv.setText("8")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.01")
            self.accel.setText("1.4")
            self.maxiter.setText("1000")
            self.frequency.setText("50")
            self.nmb_machines.setText("8")
            self.nmb_voltageR.setText("8")
            self.nmb_speedR.setText("8")
        elif self.choice == 'System 57 bus':
            pixmap = QPixmap("Resources\shemas\IEEE57bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("57")
            self.nmb_branches_total.setText("80")
            self.nmb_noeuds_pq.setText("50")
            self.nmb_noeuds_pv.setText("6")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("0")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 68 bus':
            pixmap = QPixmap("Resources\shemas\IEEE68bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("68")
            self.nmb_branches_total.setText("86")
            self.nmb_noeuds_pq.setText("52")
            self.nmb_noeuds_pv.setText("15")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.0001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("16")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
        elif self.choice == 'System 118 bus':
            pixmap = QPixmap("Resources\shemas\IEEE118bus.jpg")
            self.system_image.setPixmap(pixmap)
            self.nmb_noeuds_total.setText("118")
            self.nmb_branches_total.setText("186")
            self.nmb_noeuds_pq.setText("64")
            self.nmb_noeuds_pv.setText("53")
            self.slack_bus.setText("1")
            self.basemva.setText("100")
            self.accuracy.setText("0.0001")
            self.accel.setText("1.8")
            self.maxiter.setText("100")
            self.frequency.setText("50")
            self.nmb_machines.setText("0")
            self.nmb_voltageR.setText("0")
            self.nmb_speedR.setText("0")
    def admitance_generate_clicked(self):
        try:
            self.get_tables_values()
            self.calculate_admitance()
        except Exception as e:
            print("Error details: ",traceback.format_exc())
            QMessageBox.warning(self, "Error", "{}\nPlease verify your Data and retry \n\nREMARK: This section uses Lignes Data table and total number of noeuds".format(e))
    def impedance_generate_clicked(self):
        try:
            self.get_tables_values()
            self.calculate_impedance()
        except Exception as e:
            print("Error details: ",traceback.format_exc())
            QMessageBox.warning(self, "Error", "{}\nPlease verify your Data and retry \n\nREMARK: This section uses Lignes Data table and total number of noeuds".format(e))
    def powerflow_generate_clicked(self):
        try:
            self.get_tables_values()
            self.systemchoose()
        except Exception as e:
            print("Error details: ",traceback.format_exc())
            QMessageBox.warning(self, "Error", "{}\nPlease verify your Data and retry \n\nREMARK: This section uses Noeuds Data table and total number of noeuds".format(e))
    


    def set_tables_rows(self):
        try:
            if self.nmb_noeuds_total.text():
                x = int(self.nmb_noeuds_total.text())
            else:
                x = 0
            if self.nmb_branches_total.text():
                y = int(self.nmb_branches_total.text())
            else:
                y = 0
            if self.nmb_machines.text():
                z = int(self.nmb_machines.text())
            else:
                z = 0
            if self.nmb_voltageR.text():
                v = int(self.nmb_voltageR.text())
            else:
                v = 0
            if self.nmb_speedR.text():
                s = int(self.nmb_speedR.text())
            else:
                s = 0

            self.noeudsDATA.setRowCount(x)
            self.lignesDATA.setRowCount(y)
            self.machinesDATA.setRowCount(z)
            self.table_admitance.setRowCount(x)
            self.table_admitance.setColumnCount(x)
            self.table_impedance.setRowCount(x)
            self.table_impedance.setColumnCount(x)
            self.table_powerflow.setRowCount(x)
            self.voltageRDATA.setRowCount(v)
            self.speedRDATA.setRowCount(s)
            if self.SysTypeList.currentText() == "Custom":
                aaaa = 0
            else:
                self.datachosen()
        except:
            QMessageBox.warning(self, "Error", "Please verify the inputs")


    def get_tables_values(self):
        # Access the table widget and iterate through its items to extract values
        table1 = self.noeudsDATA  # Assuming noeudsDATA is the object name of your table
        rows = table1.rowCount()
        cols = table1.columnCount()
        values_noeuds = []
        for row in range(rows):
            row_values = []
            for col in range(cols):
                item = table1.item(row, col)
                if item is not None:
                    row_values.append(item.text())
                else:
                    row_values.append("")  # Handle empty cells

            values_noeuds.append(row_values)
        self.noeudsData = np.reshape(values_noeuds,(rows,cols))

        #########################################################################################

        table2 = self.lignesDATA
        rows = table2.rowCount()
        cols = table2.columnCount()
        values_lignes = []
        for row in range(rows):
            row_values = []
            for col in range(cols):
                item = table2.item(row, col)
                if item is not None:
                    row_values.append(item.text())
                else:
                    row_values.append("")  # Handle empty cells

            values_lignes.append(row_values)

        self.lignesData = np.reshape(values_lignes,(rows,cols))




        ############################################################################################

        table3 = self.machinesDATA  # Assuming noeudsDATA is the object name of your table
        rows = table3.rowCount()
        cols = table3.columnCount()
        values_machines = []
        for row in range(rows):
            row_values = []
            for col in range(cols):
                item = table3.item(row, col)
                if item is not None:
                    row_values.append(item.text())
                else:
                    row_values.append("")  # Handle empty cells

            values_machines.append(row_values)
        self.machinesData = np.reshape(values_machines, (rows, cols))



    def keyPressEvent(self, event) -> None:
        super().keyPressEvent(event)
        try:
            # Check keyboard input(Ctrl + V) to accomplish paste
            if event.key() == Qt.Key.Key_V and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
                selection_noeuds = self.noeudsDATA.selectedIndexes()
                selection_lignes = self.lignesDATA.selectedIndexes()
                selection_machines = self.machinesDATA.selectedIndexes()

                if selection_noeuds:
                    # Get the first selected cell position
                    row_anchor = selection_noeuds[0].row()
                    column_anchor = selection_noeuds[0].column()
                    table = self.noeudsDATA

                elif selection_lignes:
                    # Get the first selected cell position
                    row_anchor = selection_lignes[0].row()
                    column_anchor = selection_lignes[0].column()
                    table = self.lignesDATA

                elif selection_machines:
                    # Get the first selected cell position
                    row_anchor = selection_machines[0].row()
                    column_anchor = selection_machines[0].column()
                    table = self.machinesDATA

                else:
                    return  # No table selected

                # Create clipboard object to read data from clipboard
                clipboard = QApplication.clipboard()
                # Get data list from clipboard
                rows = clipboard.text().split('\n')

                # Add more rows if current row count doesn't match the new row count needed
                if table.rowCount() < row_anchor + len(rows) - 1:
                    table.setRowCount(row_anchor + len(rows) - 1)

                # Show data in table widget which gets from Excel file
                for index_row, row in enumerate(rows):
                    values = row.split("\t")
                    for index_col, value in enumerate(values):
                        item = QTableWidgetItem(value)
                        table.setItem(row_anchor + index_row, column_anchor + index_col, item)
                table.clearSelection()
            # Check keyboard input(Ctrl + C) to accomplish copy
            # Check keyboard input(Ctrl + X) to accomplish cut
            if (event.key() == Qt.Key.Key_C or event.key() == Qt.Key.Key_X) \
                    and (event.modifiers() & Qt.KeyboardModifier.ControlModifier):
                # get the selection section data
                copied_cell_noeuds = sorted(self.noeudsDATA.selectedIndexes())
                copied_cell_lignes = sorted(self.lignesDATA.selectedIndexes())
                copied_cell_machines = sorted(self.machinesDATA.selectedIndexes())

                copied_cell = copied_cell_noeuds or copied_cell_lignes or copied_cell_machines
                if not copied_cell:
                    return  # No table selected

                # Define a variable to save selected data
                copy_text = ""
                max_column = copied_cell[-1].column()
                table = self.noeudsDATA if copied_cell_noeuds else self.lignesDATA if copied_cell_lignes else self.machinesDATA
                for cell in copied_cell:
                    # Get each cell text
                    cell_item = table.item(cell.row(), cell.column())
                    if cell_item:
                        copy_text += cell_item.text()
                        # Clear data in table widget when it cuts data
                        if event.key() == Qt.Key.Key_X:
                            cell_item.setText("")

                    else:
                        copy_text += ""

                    # Format the copied data for paste into Excel file
                    if cell.column() == max_column:
                        copy_text += "\n"
                    else:
                        copy_text += "\t"

                # Save data into clipboard
                QApplication.clipboard().setText(copy_text)
                table.clearSelection()
        except Exception as e:
            print(f"Error during copy/paste: {e}")  # Handle errors gracefully









app = QApplication(sys.argv)
window3 = matrix_verification()
# window1 = Login()
window2 = ENP_RE()

img_splash = QSplashScreen(QPixmap("Resources/ENP Logo.png"))
img_splash.resize(400,350)
img_splash.show()
time.sleep(3)
# img_splash.finish(window1)

# window1.show()
window2.show()


app.exec_()
