import pandas as pd
import numpy as np
data = np.array([1, 2, 3])
df = pd.DataFrame(data, columns=['Numbers'])
print(df)

count = 0
nombre = ["Bruno", "Juan", "Pedro"]
for i in range(len(nombre)):
    print(f"Nombre {i+1}: {nombre[i]}")
    if nombre[i] == "Pedro":
        count += 1
    print(count)
if count<3:
    print("jajajaj")
    