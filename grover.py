#--

# import dlls
import matplotlib.pyplot as plt
import numpy as np

#--

# imports qiskit methods
from qiskit import IBMQ, Aer, QuantumCircuit, ClassicalRegister, QuantumRegister, execute
from qiskit.providers.ibmq import least_busy
from qiskit.quantum_info import Statevector

#--

# import drawing tools
from qiskit.visualization import plot_histogram

#--

n = 2
GroverCircuit = QuantumCircuit(n)
GroverCircuit.draw(output='mpl')

#--

GroverCircuit.h(0)
GroverCircuit.h(1)
GroverCircuit.draw(output='mpl')

#--

GroverCircuit.cz(0,1)
GroverCircuit.draw(output='mpl')

#--

def initialize_s(qc, qubits):
    GroverCircuit.h(0)
    GroverCircuit.h(1)
    return qc

#--

initialize_s(GroverCircuit, n)
GroverCircuit.z(0)
GroverCircuit.z(1)
GroverCircuit.cz(0, 1)
initialize_s(GroverCircuit, n)
## We consistently apply the gates h, z, cz, h to both qubits
GroverCircuit.draw(output='mpl')
## draw the chain

#--

## we will carry out the procedure for measuring the states at the output. Let's run it 1024 times to make sure, 
# that the probability of getting state 11 is really 100 %

GroverCircuit.measure_all()

qasm_simulator = Aer.get_backend('qasm_simulator')
shots = 1024
results = execute(GroverCircuit, backend=qasm_simulator, shots=shots).result()
answer = results.get_counts()
plot_histogram(answer)