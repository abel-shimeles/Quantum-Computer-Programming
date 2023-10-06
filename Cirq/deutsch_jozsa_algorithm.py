import numpy as np
import cirq

q_0, q_1 = cirq.LineQubit.range(2)
oracles = {
    '0': [],
    '1': [cirq.X(q_1)],
    'x': [cirq.CNOT(q_0, q_1)],
    'notx': [cirq.CNOT(q_0, q_1), cirq.X(q_1)]
}

def deutsch_algorithm(oracle):
    yield cirq.X(q_1)
    yield cirq.H(q_0), cirq.H(q_1)
    yield oracle
    yield cirq.H(q_0)
    yield cirq.measure(q_0)

for key, oracle in oracles.items():
    print('Circuit for {}...'.format(key))
    print('{}\n'.format(cirq.Circuit(deutsch_algorithm(oracle))))

simulation = cirq.Simulator()

for key, oracle in oracles.items():
    result = simulation.run(cirq.Circuit(deutsch_algorithm(oracle)), repetitions=10)
    print('\noracle: {:<4} results: {}'.format(key, result))


# Two Bit Deutsch-Jozsa Algorithm
q0, q1, q2 = cirq.LineQubit.range(3)
constant = ([], [cirq.X(q2)])
balanced = ([cirq.CNOT(q0, q2)], [cirq.CNOT(q1, q2)], [cirq.CNOT(q0, q2), cirq.CNOT(q1, q2)],
            [cirq.CNOT(q0, q2), cirq.X(q2)], [cirq.CNOT(q1, q2), cirq.X(q2)], [cirq.CNOT(q0, q2), cirq.CNOT(q1, q2), cirq.X(q2)])
for i, ops in enumerate(constant):
    print('\nConstant function {}'.format(i))
    print(cirq.Circuit(*ops).to_text_diagram(qubit_order=[q0, q1, q2]))
    print()

for i, ops in enumerate(balanced):
    print('\nBalanced function {}'.format(i))
    print(cirq.Circuit(*ops).to_text_diagram(qubit_order=[q0, q1, q2]))


# An extension of Deutsch's original algorith is the Deutsch-Josza algorithm
# which can distinguish constant from balanced functions like these using a query to
# the oracle

def your_circuit(oracle):
    # phase kickback trick
    yield cirq.X(q2), cirq.H(q2)

    # equal superposition over input bits
    yield cirq.H(q0), cirq.H(q1)

    # query the function
    yield oracle

    # interference to get result, put last qubit into |1>
    yield cirq.H(q0), cirq.H(q1), cirq.H(q2)

    # a final OR gate to put result in final qubit
    yield cirq.X(q0), cirq.X(q1), cirq.CCX(q0, q1, q2)
    yield cirq.measure(q2)


print('\nYour result on constant functions')

for oracle in constant:
    result = simulation.run(cirq.Circuit(your_circuit(oracle)), repetitions=10)
    print(result)

print('\nYour result on balanced functions')

for oracle in balanced:
    result = simulation.run(cirq.Circuit(your_circuit(oracle)), repetitions=10)
    print(result)

