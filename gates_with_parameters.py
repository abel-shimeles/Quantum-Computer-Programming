import cirq
import matplotlib.pyplot as plt
import sympy

# Getting a qubit and circuit
qubit = cirq.LineQubit(0)
circuit = cirq.Circuit()

# Getting a symbol
symbol = sympy.Symbol("t")

# Adding a parameterized gate
circuit.append(cirq.XPowGate(exponent=symbol)(qubit))

# Measuring
circuit.append(cirq.measure(qubit, key="z"))

# Displaying the circuit
print("Circuit:\n", circuit)

# Getting a sweep over parameter values
sweep = cirq.Linspace(key=symbol.name, start=0.0, stop=2.0, length=100)

# Execute the circuit for all value in the sweep
simulation = cirq.Simulator()
result = simulation.run_sweep(circuit, sweep, repetitions=1000)

# Plotting the measurement outcomes at each value in the sweep
angles = [x[0][1] for x in sweep.param_tuples()]
zeroes = [result[i].histogram(key="z")[0] / 1000 for i in range(len(result))]
plt.plot(angles, zeroes, "--", linewidth=3)

# Plotting options and formatting
plt.ylabel("Frequency of 0 Measurements")
plt.xlabel("Exponent of X gate")
plt.grid()
plt.savefig("param-sweep-cirq.pdf", format="pdf")
