import cirq

# Picking a qubit
qubit = cirq.GridQubit(0, 0)

# Creating a Circuit
circuit = cirq.Circuit(
    #  NOT Operator
    cirq.X(qubit),
    # Measurement
    cirq.measure(qubit, key='m')
)

# Displaying the circuit
print("Circuit:\n", circuit)

# Getting the simulator to execute the circuit
simulator = cirq.Simulator()

# Simulate the circuit serveral times
result = simulator.run(circuit, repetitions=10)

# Printing the Results
print("\nResults:\n", result)
