import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def create_plot(a, b, func, function_expression, root):
    if a is None or b is None:
        x_vals = np.linspace(root - 2, root + 2, 200)
    else:
        x_vals = np.linspace(a, b, 200)
    vectorized_func = np.vectorize(func)
    y_vals = vectorized_func(x_vals)

    plt.switch_backend('Agg')
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=function_expression)
    plt.axhline(y=0, color='black', linewidth=0.8, linestyle='--')
    plt.axvline(x=0, color='red', linewidth=0.8, linestyle='--')

    plt.plot(root, func(root), 'ro', label=f"Raíz aproximada: {root}")
        
    plt.title("Gráfica de la función y su raíz")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    
    buffer = BytesIO();
    plt.savefig(buffer, format='png')
    plt.close()
    buffer.seek(0)
    plot_data = base64.b64encode(buffer.read()).decode()
    return plot_data

