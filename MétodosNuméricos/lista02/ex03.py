import numpy as np

x = np.array([0.16,0.39,0.61,0.78,1.03], dtype='float32')
y = np.array([2.89,2.85,3.04,3.54,4.0], dtype='float32')

A = np.column_stack([x **i for i in range (3)])
print(f"Matriz de Design: A=\n{A}")

At = np.transpose(A)
print(f"\nMatriz de Design Transposta: At=\n{At}")

print(f"\nAt @ A =\n {At @ A}")

print(f"\nAt @ y =\n {At @ y}")

#At @ A @ a = At @ y
a = np.linalg.solve(At @ A, At @ y)
print(f"\nAt @ A @ a = At @ y:   \na= {a}")


print(f"\nf(x) = {a[0]:.4f} + {a[1]:.4f}x + {a[2]:.4f}x**2")