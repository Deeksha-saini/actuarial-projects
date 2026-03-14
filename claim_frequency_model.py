# Claim Frequency Model

import numpy as np

# number of policies
policies = 1000

# expected claim frequency
lambda_claim = 0.05

# simulate claims using Poisson distribution
claims = np.random.poisson(lambda_claim * policies)

print("Number of Policies:", policies)
print("Expected Claim Frequency:", lambda_claim)
print("Simulated Claims:", claims)
