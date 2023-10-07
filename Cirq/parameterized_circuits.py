import numpy as np
import matplotlib.pyplot as plt
import cirq
import sympy as sp

a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')
simulation = cirq.Simulator()

val = sp.Symbol('s')
pow_x_gate = cirq.X**val
circuit = cirq.Circuit()

circuit.append([pow_x_gate(a), pow_x_gate(b)])

print('Circuit with parameterized gates:')
print(circuit)
print()

for y in range(5):
    result = simulation.simulate(circuit, param_resolver={'s': y / 4.0})
    print('\ns={}: {}'.format(y, np.around(result.final_state_vector, 2)))


resolvers = [cirq.ParamResolver({'s': y / 8.0}) for y in range(9)]
circuit = cirq.Circuit()
circuit.append([pow_x_gate(a), pow_x_gate(b)])
circuit.append([cirq.measure(a), cirq.measure(b)])
results = simulation.run_sweep(program=circuit,
                              params=resolvers,
                              repetitions=10)
for i, result in enumerate(results):
    print('\nparams: {}\n{}'.format(result.params.param_dict, result))

linspace = cirq.Linspace(start=0, stop=1.0, length=11, key='x')

for p in linspace:
    print()
    print(p, '\n')



