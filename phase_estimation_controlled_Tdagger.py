qpe = QuantumCircuit(4, 3)
qpe.x(3)
qpe.draw()

for qubit in range(3):
    qpe.h(qubit)
qpe.draw()

repetitions = 1
for counting_qubit in range(3):
    for i in range(repetitions):
        qpe.cp(-math.pi/4, counting_qubit, 3); # controlled-NOT
    repetitions *= 2
qpe.draw()

#apply inverse fourier transform

qpe.barrier()
# Apply inverse QFT
qpe = qpe.compose(QFT(3, inverse=True), [0,1,2])
# Measure
qpe.barrier()
for n in range(3):
    qpe.measure(n,n)

qpe.draw()

#get results in form of histograms

aer_sim = Aer.get_backend('aer_simulator')
shots = 2048
t_qpe = transpile(qpe, aer_sim)
results = aer_sim.run(t_qpe, shots=shots).result()
answer = results.get_counts()

plot_histogram(answer)
