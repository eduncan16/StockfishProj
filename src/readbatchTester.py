import numpy as np
import matplotlib.pyplot as plt

savefile = "E:\\python projects\\Raw_data\\Alekhine_Alexander"

# Load the arrays
array1 = np.load(f"{savefile}.npy")
array2 = np.load(f"{savefile}_10_of_10.npy")
print(array1.size)
print(array2.size)
if np.allclose(array1, array2, atol=.3):
    print("True")
else:
    print("False")