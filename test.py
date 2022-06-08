import dimod
from dwave.system import LeapHybridCQMSampler
import time

# Load CQM from LP file 
st = time.time()
cqm = dimod.lp.load('test.lp')
print("\nCQM loaded.")

cqm_sampler = LeapHybridCQMSampler()
cqm_sampleset = cqm_sampler.sample_cqm(cqm)

feasible_sampleset = cqm_sampleset.filter(lambda row: row.is_feasible)
print("\nCQM sampled.")
et = time.time()

print("Run time:\t", et-st)

print("\nCQM Lowest energy:", feasible_sampleset.first.energy)
print("\tSample:")
for key, val in feasible_sampleset.first.sample.items():
    print("\t  ", key, "\t", val)