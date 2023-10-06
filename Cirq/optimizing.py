import cirq

class XZOptimizer(cirq.PointOptimizer):
    def optimization_at(self, circuit, index, op):
        if isinstance(op, cirq.GateOperation) and (op.gate == cirq.X):
            next_op_index = circuit.next_moment_operating_on(op.qubits, index + 1)
            qubit = op.qubits[0]
            if next_op_index is not None:
                next_op = circuit.operation_at(qubit, next_op_index)
                if isinstance(next_op, cirq.GateOperation) and  (next_op.gate == cirq.Z):
                    new_op = cirq.Y.on(qubit)
                    return cirq.PointOptimizationSummary(
                        clear_span = next_op_index - index + 1,
                        clear_qubits=op.qubits,
                        new_operations=[new_op])


a = cirq.NamedQubit('a')
b = cirq.NamedQubit('b')

opt = XZOptimizer()
circuit = cirq.Circuit(cirq.X(a), cirq.Z(a), cirq.CZ(a, b), cirq.X(a))

print('Before\n{}\n'. format(circuit))

opt.optimize_circuit(circuit)

print('After\n{}'.format(circuit))