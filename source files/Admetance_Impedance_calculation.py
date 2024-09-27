import csv
import numpy as np
import time
from PyQt5.QtCore import QDir
from PyQt5.QtWidgets import QTableWidgetItem, QFileDialog


class calc:
    def calculate_admitance(self):
        nbr = int(self.nmb_branches_total.text())
        nbus = int(self.nmb_noeuds_total.text())

        yserie = np.zeros((nbus, nbus), dtype=complex)
        yshunt = np.zeros((nbus, nbus), dtype=complex)
        ytransformer = np.zeros((nbus, nbus), dtype=complex)
        y = np.zeros((nbus, nbus), dtype=complex)
        for i in range(nbr):
            nl = float(self.lignesData[i, 0]) -1   # Adjust for 0-based indexing in Python
            nr = float(self.lignesData[i, 1]) -1
            r = float(self.lignesData[i, 2])
            x = float(self.lignesData[i, 3])
            b = float(self.lignesData[i, 4])
            tap = float(self.lignesData[i, 5])

            #
            nl = int(nl)
            nr = int(nr)
            # #     # Series admittance
            yserie[nl, nr] = 1 / (tap * (r + 1j * x))
            yserie[nr, nl] = yserie[nl, nr]

            #     #     # Shunt admittance
            yshunt[nl, nr] = 1j * b
            yshunt[nr, nl] = yshunt[nl, nr]

            #     #
            #     #     # Transformer admittance
            ytransformer[nl, nr] = (1 / ((r + 1j * x) * tap)) * (-1 + 1 / tap)
            ytransformer[nr, nl] = (1 / (r + 1j * x)) * (1 - 1 / tap)
            prg = (i+1)/nbr*100
            self.Admitance_progressbar.setProperty("value", prg)
        
        # # # 3. Combining admittances
        y = yserie + yshunt + ytransformer

        #     # 4. Filling the Y-matrix
        Ybus = np.zeros((nbus, nbus), dtype=complex)

        for i in range(nbus):
            for j in range(nbus):
                if i == j:
                    for n in range(nbus):
                        Ybus[i, j] = Ybus[i, j] + y[i, n]

                else:
                    Ybus[i, j] = - (yserie[i, j] + ytransformer[i, j])

        self.Ybus = Ybus #matrice admitance

        # Zbus = np.linalg.inv(Ybus)
        # self.Zbus = Zbus #matrice impedance

        table1 = self.table_admitance
        # table2 = self.table_impedance

        for i in range(nbus):
            for j in range(nbus):
                x1 = Ybus[i, j]
                # x2 = Zbus[i, j]

                real1 = format(x1.real, '.4f')
                imag1 = format(x1.imag, '.4f')
                # real2 = format(x2.real, '.4f')
                # imag2 = format(x2.imag, '.4f')
                if x1.real > 10000:
                    real_part = x1.real
                    real_scientific = "{:.3e}".format(real_part)
                    real_coefficient, real_exponent = real_scientific.split('e')
                    real_formatted = "{}*10^({})".format(real_coefficient, real_exponent)
                    real1 = real_formatted
                # if x2.real > 10000:
                #     real_part = x2.real
                #     real_scientific = "{:.3e}".format(real_part)
                #     real_coefficient, real_exponent = real_scientific.split('e')
                #     real_formatted = "{}*10^({})".format(real_coefficient, real_exponent)
                    real2 = real_formatted
                if x1.imag > 10000:
                    imaginary_part = x1.imag
                    imaginary_scientific = "{:.3e}".format(imaginary_part)
                    imaginary_coefficient, imaginary_exponent = imaginary_scientific.split('e')
                    imaginary_formatted = "{}*10^({})".format(imaginary_coefficient, imaginary_exponent)
                    imag1 = imaginary_formatted

                # if x2.imag > 10000:
                #     imaginary_part = x2.imag
                #     imaginary_scientific = "{:.3e}".format(imaginary_part)
                #     imaginary_coefficient, imaginary_exponent = imaginary_scientific.split('e')
                #     imaginary_formatted = "{}*10^({})".format(imaginary_coefficient, imaginary_exponent)
                #     imag2 = imaginary_formatted

                z1 = f"{real1} + {imag1}j"
                # z2 = f"{real2} + {imag2}j"

                if x1.real == 0:
                    real1 = "0000"
                    z1 = f"{real1} + {imag1}j"
                # if x2.real == 0:
                #     real2 = "0000"
                #     z2 = f"{real2} + {imag2}j"
                if x1.imag == 0:
                    imag1 = "0000"
                    z1 = f"{real1} + {imag1}j"
                # if x2.imag == 0:
                #     imag2 = "0000"
                #     z2 = f"{real2} + {imag2}j"

                if x1.imag < 0 :
                    z1 = f"{real1}  {imag1}j"
                # if x2.imag < 0 :
                #     z2 = f"{real2}  {imag2}j"



                table1.setItem(i, j, QTableWidgetItem(z1))
                # table2.setItem(i, j, QTableWidgetItem(z2))
        time.sleep(0.5)
        self.Admitance_progressbar.setProperty("value", 0)
    
    def calculate_impedance(self):
        # if self.impedance_calc_method.currentText() == "Ybus^(-1)":
        nbr = int(self.nmb_branches_total.text())
        nbus = int(self.nmb_noeuds_total.text())

        yserie = np.zeros((nbus, nbus), dtype=complex)
        yshunt = np.zeros((nbus, nbus), dtype=complex)
        ytransformer = np.zeros((nbus, nbus), dtype=complex)
        y = np.zeros((nbus, nbus), dtype=complex)

        for i in range(nbr):
            nl = float(self.lignesData[i, 0]) -1   # Adjust for 0-based indexing in Python
            nr = float(self.lignesData[i, 1]) -1
            r = float(self.lignesData[i, 2])
            x = float(self.lignesData[i, 3])
            b = float(self.lignesData[i, 4])
            tap = float(self.lignesData[i, 5])

            #
            nl = int(nl)
            nr = int(nr)
            # #     # Series admittance
            yserie[nl, nr] = 1 / (tap * (r + 1j * x))
            yserie[nr, nl] = yserie[nl, nr]

            #     #     # Shunt admittance
            yshunt[nl, nr] = 1j * b
            yshunt[nr, nl] = yshunt[nl, nr]

            #     #
            #     #     # Transformer admittance
            ytransformer[nl, nr] = (1 / ((r + 1j * x) * tap)) * (-1 + 1 / tap)
            ytransformer[nr, nl] = (1 / (r + 1j * x)) * (1 - 1 / tap)
            prg = (i+1)/nbr*100
            self.impedance_progressbar.setProperty("value", prg)

        # # # 3. Combining admittances
        y = yserie + yshunt + ytransformer

        #     # 4. Filling the Y-matrix
        Ybus = np.zeros((nbus, nbus), dtype=complex)

        for i in range(nbus):
            for j in range(nbus):
                if i == j:
                    for n in range(nbus):
                        Ybus[i, j] = Ybus[i, j] + y[i, n]

                else:
                    Ybus[i, j] = - (yserie[i, j] + ytransformer[i, j])

        self.Ybus = Ybus #matrice admitance

        Zbus = np.linalg.inv(Ybus)
        self.Zbus = Zbus #matrice impedance

        # table1 = self.table_admitance
        table2 = self.table_impedance

        for i in range(nbus):
            for j in range(nbus):
                # x1 = Ybus[i, j]
                x2 = Zbus[i, j]

                # real1 = format(x1.real, '.4f')
                # imag1 = format(x1.imag, '.4f')
                real2 = format(x2.real, '.4f')
                imag2 = format(x2.imag, '.4f')
                # if x1.real > 10000:
                #     real_part = x1.real
                #     real_scientific = "{:.3e}".format(real_part)
                #     real_coefficient, real_exponent = real_scientific.split('e')
                #     real_formatted = "{}*10^({})".format(real_coefficient, real_exponent)
                #     real1 = real_formatted
                if x2.real > 10000:
                    real_part = x2.real
                    real_scientific = "{:.3e}".format(real_part)
                    real_coefficient, real_exponent = real_scientific.split('e')
                    real_formatted = "{}*10^({})".format(real_coefficient, real_exponent)
                    real2 = real_formatted
                # if x1.imag > 10000:
                #     imaginary_part = x1.imag
                #     imaginary_scientific = "{:.3e}".format(imaginary_part)
                #     imaginary_coefficient, imaginary_exponent = imaginary_scientific.split('e')
                #     imaginary_formatted = "{}*10^({})".format(imaginary_coefficient, imaginary_exponent)
                #     imag1 = imaginary_formatted

                if x2.imag > 10000:
                    imaginary_part = x2.imag
                    imaginary_scientific = "{:.3e}".format(imaginary_part)
                    imaginary_coefficient, imaginary_exponent = imaginary_scientific.split('e')
                    imaginary_formatted = "{}*10^({})".format(imaginary_coefficient, imaginary_exponent)
                    imag2 = imaginary_formatted

                # z1 = f"{real1} + {imag1}j"
                z2 = f"{real2} + {imag2}j"

                # if x1.real == 0:
                #     real1 = "0000"
                #     z1 = f"{real1} + {imag1}j"
                if x2.real == 0:
                    real2 = "0000"
                    z2 = f"{real2} + {imag2}j"
                # if x1.imag == 0:
                #     imag1 = "0000"
                #     z1 = f"{real1} + {imag1}j"
                if x2.imag == 0:
                    imag2 = "0000"
                    z2 = f"{real2} + {imag2}j"

                # if x1.imag < 0 :
                #     z1 = f"{real1}  {imag1}j"
                if x2.imag < 0 :
                    z2 = f"{real2}  {imag2}j"



                # table1.setItem(i, j, QTableWidgetItem(z1))
                table2.setItem(i, j, QTableWidgetItem(z2))
        time.sleep(0.5)
        self.impedance_progressbar.setProperty("value", 0)

    def save_admitance_results(self):
        try:
            path = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/Results.csv", "Export Files (*.csv)")
            path = path[0]

            pathaAD = path.replace('.csv'," Admitance.csv")
            with open(pathaAD, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(self.Ybus)

        except:
            pass
    def saver_impedance_results(self):
        try:
            path = QFileDialog.getSaveFileName(self, 'Save File', QDir.homePath() + "/Results.csv", "Export Files (*.csv)")
            path = path[0]

            pathIMD = path.replace('.csv'," Impedance.csv")
            with open(pathIMD, 'w', newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                csvwriter.writerows(self.Ybus)

        except:
            pass
    def fill_matrices(self):
        nbus = int(self.nmb_noeuds_total.text())
        self.ybus.setRowCount(nbus)
        self.ybus.setColumnCount(nbus)
        self.zbus.setRowCount(nbus)
        self.zbus.setColumnCount(nbus)
        self.ybus_zbus.setRowCount(nbus)
        self.ybus_zbus.setColumnCount(nbus)
        self.calculate_admitance()
        self.calculate_impedance()
        for i in range(nbus):
            for j in range(nbus):
                item1 = QTableWidgetItem(str(self.Ybus[i,j+1]))
                self.ybus.setItem(i, j, item1)
                item2 = QTableWidgetItem(str(self.Zbus[i,j+1]))
                self.zbus.setItem(i, j, item2)
    def click_verify(self):
        nbus = int(self.nmb_noeuds_total.text())
        self.ybus.setRowCount(nbus)
        self.ybus.setColumnCount(nbus)
        self.zbus.setRowCount(nbus)
        self.zbus.setColumnCount(nbus)
        self.ybus_zbus.setRowCount(nbus)
        self.ybus_zbus.setColumnCount(nbus)
        self.calculate_admitance()
        self.calculate_impedance()
        for i in range(nbus):
            for j in range(nbus):
                item3 = self.Ybus[i,j+1] - self.Zbus[i,j+1]
                self.ybus_zbus.setItem(i, j, str(item3))
        verified = 1
        for i in range(nbus):
            for j in range(nbus):
                if float(self.ybus_zbus.item(i, j).text()) != 0:
                    verified = 0
        
        if verified == 1:
            self.verified_or_not.setText("Verified: Ybus = Zbus^(-1)")
        else:
            self.verified_or_not.setText("NOT Verified: Ybus != Zbus^(-1)")