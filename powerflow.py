import numpy as np
class powerflow:
    def gauss_seidel(self):
        nbus = int(self.nmb_noeuds_total.text())
        row_count = self.noeudsDATA.rowCount()
        col_count = self.noeudsDATA.columnCount()
        data = []
        for row in range(row_count):
            row_data = []
            for col in range(col_count):
                item = self.noeudsDATA.item(row, col)
                if item is not None and item.text():
                    row_data.append(float(item.text()))
                else:
                    row_data.append(0.0)  # Assuming default value is 0
            data.append(row_data)
        Nbusdata = np.array(data)

        delta = Nbusdata[:, 2] * (np.pi / 180)
        v = Nbusdata[:, 1] * (np.cos(delta) + 1j * np.sin(delta))
        print(v)
        P1 = Nbusdata[:, 3]
        Q1 = Nbusdata[:, 4]
        Pg = Nbusdata[:, 5]
        Qg = Nbusdata[:, 6]
        Qmin = Nbusdata[:, 7]
        Qmax = Nbusdata[:, 8]
        Qc = Nbusdata[:, 9]
        P = Pg - P1
        Q = Qg - Q1 + Qc
        tol = 0.1
        k = 1
        # Initializations
        accuracy = float(self.accuracy.text())
        maxiter = float(self.maxiter.text())
        accel = float(self.accel.text())
        self.calculate_admitance()
        
        # Main loop
        while tol > accuracy and k < maxiter:
            v1 = v.copy()
            for m in range(nbus):
                # la somme des produits
                # s1 = np.dot(self.Ybus[m, :m], v[:m])
                s1 = 0
                for j in range(0, m):
                    print(v[j,0])
                    s1 += self.Ybus[m,j]*v[j,0]
                    
                s2 = np.dot(self.Ybus[m, m+1:], v[m+1:])
                prod = (P[m] - 1j * Q[m]) / np.conj(v[m])
                if Nbusdata[m, 0] == 0:  # pour PQ
                    v[m] = (prod - s1 - s2) / self.Ybus[m, m] # l'équation (2) dans mon resumé
                    v[m] = v1[m] + accel * (v[m] - v1[m])
                elif Nbusdata[m, 0] == 2:  # pour PV
                    Q[m] = -np.imag(np.conj(v[m]) * np.dot(self.Ybus[m, :], v))
                    prod = (P[m] - 1j * Q[m]) / np.conj(v[m])
                    delta = np.angle((prod - s1 - s2) / self.Ybus[m, m])
                    v[m] = abs(v1[m]) * (np.cos(delta) + 1j * np.sin(delta))
            tol = np.max(np.abs(np.abs(v) - np.abs(v1)))
            k += 1
        # print(self.Ybus[m,j])
        # print(v[j,0])
        # print(s1)
        # print(s2)
        # Calcul des puissances actives et réactives pour chaque noeud
        for i in range(nbus):
            s = np.conj(v[i,0]) * np.dot(self.Ybus[i, :], v)
            P[i] = np.real(s)
            Q[i] = -np.imag(s)

        # Update Qg and Pg
        for i in range(nbus):
            if Nbusdata[i, 0] == 2:
                Qg[i] = Q[i] + Q1[i] - Qc[i]
            elif Nbusdata[i, 0] == 1:  # Slack bus
                Pg[i] = P[i] + P1[i]
                Qg[i] = Q[i] + Q1[i]

        # Update Nbusdata
        Nbusdata[:, 1] = np.abs(v)
        Nbusdata[:, 2] = np.angle(v) * (180 / np.pi)
        Nbusdata[:, 5] = Pg
        Nbusdata[:, 6] = Qg
        for j in range(3, 10):
            Nbusdata[:, j] *= float(self.basemva.text())

        # Compute totals
        # PT = np.sum(Nbusdata[:, 5])
        # QT = np.sum(Nbusdata[:, 6])
        # PlT = np.sum(Nbusdata[:, 3])
        # QlT = np.sum(Nbusdata[:, 4])
        # pertesP = PT - PlT  # pertes actives
        # pertesR = QT - QlT  # pertes reactives
        # p = (pertesP / PT) * 100  # Pourcentage des pertes actives
        # Nbusdata = np.abs(Nbusdata)
        # V = v
        #****************************************** !!! **************************

        # Nbusdata is a copy of busdata to manipulate while keeping the original busdata matrix intact
        Nbusdata = busdata.copy()

        # Converting to per unit system
        for j in range(4, 11):
            Nbusdata[:, j] = busdata[:, j] / basemva

        delta = Nbusdata[:, 3] * (np.pi / 180)
        V = Nbusdata[:, 2] * (np.cos(delta) + 1j * np.sin(delta))

        # Y is the admittance matrix
        Y = Ybus

        # Loading data
        Pload = Nbusdata[:, 4]  # Active powers of loads at each node
        Qload = Nbusdata[:, 5]  # Reactive powers of loads at each node
        Pgen = Nbusdata[:, 6]   # Active powers of generation at each node
        Qgen = Nbusdata[:, 7]   # Reactive powers of generation at each node
        Qmin = Nbusdata[:, 8]   # Minimum limits of reactive power generation (PV and slack nodes)
        Qmax = Nbusdata[:, 9]   # Maximum limits of reactive power generation (PV and slack nodes)
        Qcap = Nbusdata[:, 10]  # Reactive power compensations

        # Calculating active and reactive powers
        P = Pgen - Pload
        Q = Qgen - Qload + Qcap

        error = 1  # Initializing error
        k = 1  # Iteration counter

        while error > accuracy and k < maxiter:
            Vold = V.copy()
            for m in range(nbus):  # Loop through nodes
                s1 = np.dot(Y[m, :m], V[:m])  # Summation Y*V from 1 to m-1
                s2 = np.dot(Y[m, m + 1:nbus], V[m + 1:nbus])
                prod = (P[m] - 1j * Q[m]) / np.conj(V[m])

                if Nbusdata[m, 1] == 0:  # Special PQ nodes
                    V[m] = (prod - s1 - s2) / Y[m, m]
                    V[m] = Vold[m] + accel * (V[m] - Vold[m])  # Acceleration of convergence for PV nodes

                elif Nbusdata[m, 1] == 2:  # Special PV nodes
                    Q[m] = -np.imag(np.conj(V[m]) * np.dot(Y[m, :], V))
                    prod = (P[m] - 1j * Q[m]) / np.conj(V[m])
                    delta[m] = np.angle((prod - s1 - s2) / Y[m, m])
                    V[m] = abs(Vold[m]) * (np.cos(delta[m]) + 1j * np.sin(delta[m]))

            error = np.max(np.abs(abs(V) - abs(Vold)))  # Error calculation
            k += 1  # Iteration counter

        # Calculating active and reactive powers at each node
        for i in range(nbus):
            s = np.conj(V[i]) * np.dot(Y[i, :], V)
            P[i] = np.real(s)
            Q[i] = -np.imag(s)

        # Data collection
        for i in range(nbus):
            if Nbusdata[i, 1] == 2:  # Special PV node
                Qgen[i] = Q[i] + Qload[i] - Qcap[i]
            elif Nbusdata[i, 1] == 1:  # Special Slack bus
                Pgen[i] = P[i] + Pload[i]
                Qgen[i] = Q[i] + Qload[i]

        # Updating Nbusdata matrix
        Nbusdata[:, 2] = np.abs(V)
        Nbusdata[:, 3] = np.angle(V) * (180 / np.pi)
        Nbusdata[:, 6] = Pgen
        Nbusdata[:, 7] = Qgen

        # Converting back to normal system from per unit
        for j in range(4, 11):
            Nbusdata[:, j] = Nbusdata[:, j] * basemva


    def newton_raphson(self):
        
        nbus = int(self.nmb_noeuds_total.text())
        npv = int(self.nmb_noeuds_pv.text())
        npq = int(self.nmb_noeuds_pq.text())
        accuracy = float(self.accuracy.text())
        maxiter = float(self.maxiter.text())
        basemva = float(self.basemva.text()) 
        accel = float(self.accel.text())

        noeudsDATA = []
        tdata = []
        for row in range(self.noeudsDATA.rowCount()):
            for col in range(self.noeudsDATA.columnCount()):
                tdata.append(float(self.noeudsDATA.item(row, col).text()))
            noeudsDATA.append(tdata)
            tdata = []
        for index, row in enumerate(noeudsDATA):
            row.insert(0, index)
        Nbusdata = np.array(noeudsDATA, dtype=float) # Nbusdata une copie de la matrice busdata afin de pouvoir manipuler tout en gardant la matrice originale busdata 
        
        self.calculate_admitance()  # Calcul de la matrice admittance
        
        #***** Declaration of variables *****#
        Ybus = self.Ybus
        v = Nbusdata[:,2]
        v = v.reshape(nbus,1)
        v_angle = Nbusdata[:,3]
        v_angle = v_angle.reshape(nbus,1)
        Pload = Nbusdata[:,4]#/basemva
        Qload = Nbusdata[:, 5]#/basemva
        Pgen = Nbusdata[:, 6]#/basemva
        Qgen = Nbusdata[:, 7]#/basemva
        Qmin = Nbusdata[:, 8]#/basemva
        Qmax = Nbusdata[:, 9]#/basemva
        Qcap = Nbusdata[:, 10]#/basemva  # Puissances réactives de compensation en radian

        P = Pgen-Pload
        Q = Qgen-Qload
        P = P.reshape(nbus,1)
        Q = Q.reshape(nbus,1)

        Pcal = np.zeros((nbus,1))
        Qcal = np.zeros((nbus,1))
        delta_P  = np.zeros((nbus,1))
        delta_Q  = np.zeros((nbus,1))
        delta_e_f = np.zeros((2*nbus,1))

        J1 = np.zeros((nbus, nbus), dtype=complex)
        J2 = np.zeros((nbus, nbus), dtype=complex)
        J3 = np.zeros((nbus, nbus), dtype=complex)
        J4 = np.zeros((nbus, nbus), dtype=complex)

        #***** converting v and v_angle to a v_complex *****#
        v_complex = np.zeros((nbus,1), dtype=complex)
        for i in range(nbus):
            v_angle[i,0] = v_angle[i,0] * (np.pi / 180)
        for i in range(nbus):
            v_complex[i,0] = v[i,0] * np.cos(v_angle[i,0]) + 1j*v_angle[i,0]*np.sin(v_angle[i,0])
        #***** declaration ei et fi la partie real et imaginaire de v. v2 is the squar of v (v^2) and G, B the real and imaginary parts of Ybus *****#
        e  = np.zeros((nbus,1))
        f  = np.zeros((nbus,1))
        c  = np.zeros((nbus,1))
        d  = np.zeros((nbus,1))
        s  = np.zeros((nbus,1), dtype=complex) #la puissance apparent
        G = Ybus.real
        B = Ybus.imag
        #***** calcule de ei et fi de chaque noeud *****#
        for i in range(nbus):
            e[i,0] = v_complex[i,0].real
            f[i,0] = v_complex[i,0].imag

        # #***** block de calcule *****#
        iteration = 0 
        error = 1
        while iteration < int(maxiter) and error > float(accuracy):
            for i in range(nbus): 
                sumPi  = 0
                sumQi  = 0
                sumc   = 0
                sumd   = 0 
                for j in range(nbus):
                    sumPi  += e[i,0]*(G[i,j]*e[j,0] + B[i,j]*f[j,0]) + f[i,0]*(G[i,j]*f[j,0] - B[i,j]*e[j,0])
                    sumQi  += f[i,0]*(G[i,j]*e[j,0] + B[i,j]*f[j,0]) - e[i,0]*(G[i,j]*f[j,0] - B[i,j]*e[j,0])
                    if i != j:
                        sumc += e[j,0]*G[i,j] + f[j,0]*B[i,j]
                        sumd += f[j,0]*G[i,j] - e[j,0]*B[i,j]
                Pcal[i,0] = sumPi
                Qcal[i,0] = sumQi
                c[i,0]    = e[i,0]*G[i,i] + f[i,0]*B[i,i] + sumc
                d[i,0]    = f[i,0]*G[i,i] - e[i,0]*B[i,i] + sumd
                delta_P[i,0] = P[i,0] - Pcal[i,0]
                delta_Q[i,0] = Q[i,0] - Qcal[i,0]
                
            for i in range(nbus):
                for j in range(nbus):
                    if i == j:
                        J1[i,i] = e[i,0]*G[i,i] - f[i,0]*B[i,i] + c[i,0]
                        J2[i,i] = e[i,0]*B[i,i] + f[i,0]*G[i,i] + d[i,0]
                        J3[i,i] = e[i,0]*B[i,i] + f[i,0]*G[i,i] - d[i,0]
                        J4[i,i] = -(e[i,0]*G[i,i] - f[i,0]*B[i,i]) + c[i,0]
                    else:
                        J1[i,j] = e[i,0]*G[i,j] - f[i,0]*B[i,j] 
                        J2[i,j] = e[i,0]*B[i,j] + f[i,0]*G[i,j]
                        J3[i,j] = e[i,0]*B[i,j] + f[i,0]*G[i,j]
                        J4[i,j] = -(e[i,0]*G[i,j] - f[i,0]*B[i,j])

            J = np.block([[J1, J2], [J3, J4]])
            J_inv = np.linalg.inv(J)

            delta_P_Q = np.block([[delta_P],[delta_Q]])
            delta_e_f = J_inv @ delta_P_Q

            delta_e = delta_e_f[:nbus,0]
            delta_e = delta_e.reshape(nbus,1)
            delta_f = delta_e_f[nbus:,0]
            delta_f = delta_f.reshape(nbus,1)
            for i in range(nbus):
                e[i,0] = e[i,0] + accel * delta_e[i,0]
                f[i,0] = f[i,0] + accel * delta_f[i,0]
            

            error = np.max(delta_P_Q)
            iteration +=1
            print(iteration)
    
        for i in range(nbus):
            v_complex[i,0] = e[i,0] +1j*f[i,0]
            v[i,0]       = np.abs(v_complex[i,0])
            v_angle[i,0] = np.angle(v_complex[i,0]) * (180/np.pi)
            sum = 0
            for j in range(nbus):
                sum += Ybus[i,j]*v_complex[j,0]
            s[i,0]       = np.conj(v_complex[i,0])* sum

        #********************************************* !!! *******************************

        # Calculation for generator nodes
        Pg[0, 0] = np.real(np.conj(V[0]) * Ybus[0, :] * V)
        Qg[0, 0] = -np.imag(np.conj(V[0]) * Ybus[0, :] * V)

        PP = np.conj(V[1:(npv + 1)])
        BB = Ybus[1:(npv + 1), :] * V
        cc = PP * BB
        Qg[1:(npv + 1)] = Ql[1:(npv + 1)] - np.imag(cc)
        delta[1:(npv + 1)] = np.angle(V[1:(npv + 1)])

        # Calculation for PQ nodes
        delta[(npv + 1):nbus] = np.angle(V[(npv + 1):nbus])

        # Modifications in the Nbusdata matrix
        Nbusdata[:, 2] = v
        Nbusdata[:, 3] = delta * (180 / np.pi)
        Nbusdata[:, 6] = Pg
        Nbusdata[:, 7] = Qg
        Nbusdata[:, 4] = Pl
        Nbusdata[:, 5] = Ql

        R = busdata.copy()
        for i in range(nbus):
            for j in range(nbus):
                if Nbusdata[j, 0] == busdata[i, 0]:
                    R[i, :] = Nbusdata[j, :]
                    break

        Nbusdata = R
        Ybus = A

        for j in range(4, 11):
            Nbusdata[:, j] *= basemva

        PT = np.sum(Nbusdata[:, 6])
        QT = np.sum(Nbusdata[:, 7])
        PlT = np.sum(Nbusdata[:, 4])
        QlT = np.sum(Nbusdata[:, 5])

        pertesP = PT - PlT  # Active losses
        pertesR = QT - QlT  # Reactive losses
        p = (pertesP / PT) * 100  # Percentage of active losses

        Nbusdata = np.abs(Nbusdata)

    def FDLF(self):

        # Nbusdata is a copy of busdata to manipulate while keeping the original busdata matrix intact
        indSB = np.where(busdata[:, 1] == 1)[0]  # Index of the Slack bus
        Nbusdata = busdata[indSB, :]

        # Adding PV nodes to Nbusdata
        for i in range(nbus):
            if busdata[i, 1] == 2:
                Nbusdata = np.vstack((Nbusdata, busdata[i, :]))

        # Adding PQ nodes to Nbusdata
        for i in range(nbus):
            if busdata[i, 1] == 0:
                Nbusdata = np.vstack((Nbusdata, busdata[i, :]))

        # Normalizing power columns
        for j in range(4, 11):
            Nbusdata[:, j] = Nbusdata[:, j] / basemva

        # Angles of node voltages in radians
        delta = Nbusdata[:, 3] * (np.pi / 180)

        # Voltages amplitudes of nodes
        v = Nbusdata[:, 2]

        # Rearranging admittance matrix according to Nbusdata order
        D = np.zeros((nbus, nbus))
        for i in range(nbus):
            for j in range(nbus):
                D[i, j] = Ybus[int(Nbusdata[i, 0]) - 1, int(Nbusdata[j, 0]) - 1]
        Y = D

        G = np.real(Y)
        B = -np.imag(Y)

        # Loading data
        Pload = Nbusdata[:, 4]
        Qload = Nbusdata[:, 5]
        Pgen = Nbusdata[:, 6]
        Qgen = Nbusdata[:, 7]
        Qmin = Nbusdata[:, 8]
        Qmax = Nbusdata[:, 9]
        Qcap = Nbusdata[:, 10]

        # Specified powers of PV and PQ nodes
        Pspec = Pgen[1:nbus] - Pload[1:nbus]
        Qspec = Qgen[npv + 1:nbus] - Qload[npv + 1:nbus] + Qcap[npv + 1:nbus]
        vspec = v[1:npv + 1]

        Fspec = np.concatenate((Pspec, Qspec, vspec))

        # Initialization
        ddelta = np.zeros((nbus - 1, 1))
        dv = np.zeros((npq, 1))
        P = np.zeros((nbus, 1))
        Q = np.zeros((nbus, 1))
        Pcal = np.zeros((nbus - 1, 1))
        Qcal = np.zeros((npq, 1))
        vcal = np.zeros((npv, 1))
        Fcal = np.zeros((2 * (npq + npv), 1))
        F = np.zeros((2 * (npv + npq), 1))

        J1 = B[1:nbus, 1:nbus]
        J4 = B[npv + 1:nbus, npv + 1:nbus]
        invJ1 = np.linalg.inv(J1)
        invJ4 = np.linalg.inv(J4)

        error = 1
        k = 0

        while error > accuracy and k < maxiter:
            for i in range(nbus):
                sumP = 0
                sumQ = 0
                for j in range(nbus):
                    sumP += v[j] * (G[i, j] * np.cos(delta[j] - delta[i]) + B[i, j] * np.sin(delta[j] - delta[i]))
                    sumQ += v[j] * (G[i, j] * np.sin(delta[j] - delta[i]) - B[i, j] * np.cos(delta[j] - delta[i]))
                P[i] = v[i] * sumP
                Q[i] = -v[i] * sumQ

            Pcal = P[1:nbus]
            Qcal = Q[npv + 1:nbus]
            vcal = v[1:npv + 1]

            Fcal[:nbus - 1] = Pspec - Pcal
            Fcal[nbus - 1:nbus - 1 + npq] = Qspec - Qcal
            Fcal[nbus - 1 + npq:] = vspec - vcal

            F = Fspec - Fcal

            for i in range(1, nbus):
                ddelta[i - 1] = np.dot(invJ1[i - 1], (Pspec - Pcal) / v[1:nbus])

            for i in range(npv + 1, nbus):
                dv[i - (npv + 1)] = np.dot(invJ4[i - (npv + 1)], (Qspec - Qcal) / v[npv + 1:nbus])

            delta[1:nbus] += ddelta.ravel()
            v[npv + 1:nbus] += dv.ravel()

            k += 1
            error = np.max(np.abs(F))

        # Data collection
        V = v * (np.cos(delta) + 1j * np.sin(delta))
        Pgen[0] = np.real(np.conj(V[0]) * Y[0, :] * V)
        Qgen[0] = -np.imag(np.conj(V[0]) * Y[0, :] * V)

        AA = np.conj(V[1:npv + 1])
        BB = np.dot(Y[1:npv + 1, :], V)
        cc = AA * BB
        Qgen[1:npv + 1] = Qload[1:npv + 1] - np.imag(cc)

        # Modifications in the Nbusdata matrix
        Nbusdata[:, 2] = v
        Nbusdata[:, 3] = delta * (180 / np.pi)
        Nbusdata[:, 6] = Pgen
        Nbusdata[:, 7] = Qgen

        # Rearranging Nbusdata matrix
        D = busdata.copy()
        for i in range(nbus):
            for j in range(nbus):
                if Nbusdata[j, 0] == busdata[i, 0]:
                    D[i, :] = Nbusdata[j, :]
        Nbusdata = D

        # Rearranging Nbusdata matrix
        for j in range(4, 11):
            Nbusdata[:, j] = Nbusdata[:, j] * basemva




