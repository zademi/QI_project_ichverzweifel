from qiskit import IBMQ, QuantumCircuit, execute,  Aer
from qiskit.result import marginal_counts
from qiskit.providers.ibmq.job import job_monitor
from qiskit.tools.visualization import plot_histogram
import matplotlib.pyplot as plt
from math import pi

IBMQ.load_account()
provider = IBMQ.get_provider(hub='ibm-q', group='open', project='main')
s_provider = 'ibmq_bogota'
backend = provider.get_backend(s_provider)

#GHZ generation
qc_simp = QuantumCircuit(5, 5)
qc_simp.h(2)
qc_simp.cx([2, 2, 1, 3, 0, 4], [1, 3, 0, 4, 1, 3])

#1st round without error
qc_simp.barrier([0, 1, 2, 3, 4])
qc_simp.x(2)
qc_simp.cx([0, 4, 2, 2], [1, 3, 1, 3])
qc_simp.measure([1, 3], [0, 1])
#qc_simp.draw('mpl')
#plt.show()

#2nd round with x error on qubit 0
qc_simp.barrier([0, 1, 2, 3, 4])
qc_simp.cx([0, 4, 2, 2], [1, 3, 1, 3])
qc_simp.measure([1, 3], [2, 3])
qc_simp.draw('mpl')
plt.show()


simp_job = execute(qc_simp, backend=backend, shots=1024)
print(simp_job.job_id()) #prints ID I can search for on the IBM website
job_monitor(simp_job)


counts_anscilla1 = marginal_counts(simp_job.result(), indices=[0, 1]).get_counts()
print("Results_anscilla1: ", counts_anscilla1)

counts_anscilla2 = marginal_counts(simp_job.result(), indices=[2, 3]).get_counts()
print("Results_anscilla2: ", counts_anscilla2)


plot_histogram(counts_anscilla1, title='anscilla measurements after one round')
plot_histogram(counts_anscilla2, title='anscilla measurements after second round')

plt.show()

