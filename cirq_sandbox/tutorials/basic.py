"""
Cirq has three main ways of defining qubits:

* cirq.NamedQubit: used to label qubits by an abstract name
* cirq.LineQubit: qubits labelled by number in a linear array
* cirq.GridQubit: qubits labelled by two numbers in a rectangular lattice.
"""
import cirq


# Using named qubits can be useful for abstract algorithms
# as well as algorithms not yet mapped onto hardware.
q0 = cirq.NamedQubit('source')
q1 = cirq.NamedQubit('target')

# Line qubits can be created individually
q3 = cirq.LineQubit(3)

# Or created in a range
# This will create LineQubit(0), LineQubit(1), LineQubit(2)
q0, q1, q2 = cirq.LineQubit.range(3)

# Grid Qubits can also be referenced individually
q4_5 = cirq.GridQubit(4,5)

# Or created in bulk in a square
# This will create 16 qubits from (0,0) to (3,3)
qubits = cirq.GridQubit.square(4)