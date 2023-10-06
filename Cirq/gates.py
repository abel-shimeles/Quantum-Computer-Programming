import numpy as np
import matplotlib.pyplot as plt
import cirq 

q0, q1, q2 = cirq.LineQubit.range(3)
simulation = cirq.Simulator()

operations = [
    cirq.X(q0),
    cirq.Y(q1),
    cirq.Z(q2),
    cirq.CZ(q0,q1),
    cirq.CNOT(q1,q2),
    cirq.H(q0),
    cirq.T(q1),
    cirq.S(q2),
    cirq.CCZ(q0, q1, q2),
    cirq.SWAP(q0, q1),
    cirq.CSWAP(q0, q1, q2),
    cirq.CCX(q0, q1, q2),
    cirq.ISWAP(q0, q1),
    cirq.rx(0.5 * np.pi)(q0),
    cirq.ry(0.5 * np.pi)(q1),
    cirq.ry(0.5 * np.pi)(q2),
    (cirq.X**0.5)(q0),
]

print(cirq.Circuit(*operations))
print('\n', cirq.unitary(cirq.CNOT))
print('\n', cirq.unitary(cirq.rx(0.5 * np.pi)))

# Simulate Circuit Moment by Moment
a = cirq.NamedQubit('a')
circuit = cirq.Circuit(*[cirq.rx(np.pi / 50.0)(a) for theta in range(200)])
print('\nCircuit is a bunch of small rotations about Pauli X axis:')
print('{}\n'.format(circuit))

p_0 = []
z = []
repetitions = 100
print('\nWe step through the circuit and plot the z component of the vector '
      'as a function of index of the moment being stepped over.')

for i, step in enumerate(simulation.simulate_moment_steps(circuit)):
    samples = step.sample([a], repetitions=repetitions)
    prob_0 = np.sum(samples, axis=0)[0] / repetitions
    z.append(i)
    p_0.append(prob_0)

plt.plot(z, p_0, 'o')
plt.savefig('gates.pdf')

# Custom Gate Implementation
class RotationalGate(cirq.Gate):
    def __init__(self, theta):
        super(RotationalGate, self)
        self.theta = theta

    def _num_qubits_(self):
        return 1

    def _unitary_(self):
        return np.array([
            [np.cos(self.theta), np.sin(self.theta)],
            [np.sin(self.theta), -np.cos(self.theta)]
        ]) / np.sqrt(2)

    def _circuit_diagram_info_(self, args):
        return f"R({self.theta})"


a = cirq.NamedQubit('a')
rg = RotationalGate(theta=0.2)

circuit = cirq.Circuit(rg.on(cirq.LineQubit(0)))

print('Custom Rotation Gate circuit:\n', circuit)

