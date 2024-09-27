
# ENP RE - Electrical Network Parameters Calculation Software

![source files/Logo-ENP.png](source files/Logo-ENP.png)

### Overview
**ENP RE** is a Python-based Windows software designed for analyzing and calculating electrical network parameters. It offers tools for generating admittance and impedance matrices, as well as running power flow simulations using Gauss-Seidel, Newton-Raphson, and Fast Decoupled Load Flow (FDLF) methods. This software is aimed at students, engineers, and professionals working with electrical power systems, providing both numerical solutions and easy-to-use interfaces.

### Features
- **Admittance and Impedance Matrix Calculation:**
  - Calculates the Y-bus (admittance) and Z-bus (impedance) matrices for electrical grids.
- **Power Flow Simulation:**
  - Simulates the power flow in the network using:
    - **Gauss-Seidel**
    - **Newton-Raphson**
    - **Fast Decoupled Load Flow (FDLF)**
- **Graphical User Interface (GUI):**
  - Provides an easy-to-navigate interface with visualizations of the input data, matrix generation, and simulation results.
- **Data Input/Output:**
  - Users can input system data for calculations and save the output results.
- **License Key Authentication:**
  - The software requires a license key to run. Example serial code: `3255-6021-8748-1498`.

### Installation Guide

#### System Requirements:
- **Operating System:** Windows 7 or later
- **Python Version:** Python 3.x
- **Dependencies:**
  - `numpy`
  - `matplotlib`
  - `scipy`
  - `PyQt5` (for GUI)

#### Steps to Install:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ENP-RE.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ENP-RE
   ```
3. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the software:
   ```bash
   python ENP\ RE.py
   ```

### Usage Instructions
1. **Launching the Software:**
   After installing the necessary dependencies, run the main Python script `ENP RE.py`. You will be prompted to enter a serial code. Use the provided code: `3255-6021-8748-1498`.

2. **Navigating the Interface:**
   - **Main Page:** Choose the type of network and input the relevant system data.
   - **Admittance/Impedance Matrices:** Select options to calculate and view the Y-bus and Z-bus matrices.
   - **Power Flow Simulation:** Choose one of the methods (Gauss-Seidel, Newton-Raphson, or FDLF) and run simulations.
   - **Saving Results:** Results from the simulation can be saved for further analysis.

3. **Source Code Overview:**
   - **`matrices_verifing.py`:** Verifies the input matrices for validity.
   - **`powerflow.py`:** Contains algorithms for power flow simulations using Gauss-Seidel, Newton-Raphson, and FDLF methods.
   - **`RE_UI.py`:** Defines the graphical user interface (GUI) using PyQt5.
   - **`SysData.py`:** Handles the system data input and management.
   - **`Admetance_Impedance_calculation.py`:** Performs the calculations for Y-bus and Z-bus matrices.
   - **`Login_interface.py`:** Manages user login and serial key validation.
   - **`ENP RE.py`:** Main script that integrates all components and runs the software.

### Screenshots
Below are some screenshots to help you navigate through the interface:

- **Main Interface:**
  ![Main Page](Logo-ENP.png)
- **Matrix Calculations:**
  Displays the calculated Y-bus and Z-bus matrices.

- **Simulation Results:**
  Power flow analysis results, including voltage levels, currents, and losses.

*More images can be found in the `/screenshots` folder.*

### Contributions
Contributions to improve **ENP RE** are welcome! Here’s how you can contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

### License
This project is licensed under the MIT License - see the `LICENSE` file for details.

### Contact
For any questions or support, feel free to open an issue or contact the project maintainers.

---

### GitHub Repository Description
**ENP RE - Electrical Network Parameters Calculation Software**

A Python-based software for Windows that calculates electrical network admittance and impedance matrices, runs power flow simulations using Gauss-Seidel, Newton-Raphson, and FDLF methods, and provides an intuitive graphical interface for easy usage.
