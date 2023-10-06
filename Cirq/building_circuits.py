import cirq

a = cirq.NamedQubit("a")
b = cirq.NamedQubit("b")
c = cirq.NamedQubit("c")

operations = [cirq.H(a), cirq.H(b), cirq.CNOT(b,c), cirq.H(b)]

circuit = cirq.Circuit(*operations)

print(circuit)

for i, moment in enumerate(circuit):
    print('\nMoment {}: {}'.format(i, moment))

print(repr(circuit))


def xor_swap(a, b):
    yield cirq.CNOT(a, b)
    yield cirq.CNOT(b, a)
    yield cirq.CNOT(a, b)


def left_rotate(qubits):
    for i in range(len(qubits) - 1):
        a, b = qubits[i:i+2]
        yield xor_swap(a, b)


line = cirq.LineQubit.range(5)
print()
print(cirq.Circuit(left_rotate(line)))

# Creating a Circuit

a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')
c = cirq.NamedQubit('c')
circuit = cirq.Circuit()
circuit.append([cirq.CZ(a, b), cirq.H(c), cirq.H(a)])
circuit.append([cirq.H(b), cirq.CZ(b, c), cirq.H(b), cirq.H(a), cirq.H(a)], strategy=cirq.InsertStrategy.NEW_THEN_INLINE)

print()
print(circuit)
