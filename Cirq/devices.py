import cirq
import cirq_google

q55 = cirq.GridQubit(5, 5)
q56 = cirq.GridQubit(5, 6)
q66 = cirq.GridQubit(6, 6)
q67 = cirq.GridQubit(6, 7)

ops = [cirq.CZ(q55, q56), cirq.CZ(q66, q67)]

print(cirq_google.Sycamore)

circuit = cirq.Circuit()
circuit.append(ops)

print(circuit)


