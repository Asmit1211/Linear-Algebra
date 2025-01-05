import numpy as np
# Function for displaying the conjugate of a complex number
def conjugate(z):
    return np.conj(z)
z1 = 3 + 2j
# Get the conjugate of z1
conj_z1 = conjugate(z1)
print(f"Conjugate of {z1} is {conj_z1}")