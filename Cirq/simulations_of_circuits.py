import numpy as np
import cirq

a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')

def basic_circuit(measure=True):
    sqrt_x = cirq.X**0.5
    cz = cirq.CZ
    yield sqrt_x(a), sqrt_x(b)
    yield cz(a, b)
    yield sqrt_x(a), sqrt_x(b)

    if measure:
        yield cirq.measure(a, b)


simulation = cirq.Simulator()
circuit = cirq.Circuit(basic_circuit(measure=False))
result = simulation.simulate(circuit, qubit_order=[a,b])

print(circuit)
print('\nMeasurement results:\n', result)
print('\nWavefunction:\n', np.around(result.final_state_vector, 3))
print('\nDirac notation:\n', result.dirac_notation())

