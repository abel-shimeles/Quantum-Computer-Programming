import cirq

# Getting qubits and circuit
qreg = [cirq.LineQubit(x) for x in range(2)]
circuit = cirq.Circuit()

# Adding the Bell State preparation circuit
circuit.append([cirq.H(qreg[0]), cirq.CNOT(qreg[0], qreg[1])])

# Displaying the Circuit
print("Circuit:\n", circuit)

# Adding Measurements
circuit.append(cirq.measure(*qreg, key="z"))

# Simulating the circuit
simulation = cirq.Simulator()
result = simulation.run(circuit, repetitions=100)

# Displaying the outcomes
print("\nMeasurements:\n", result.histogram(key="z"))
