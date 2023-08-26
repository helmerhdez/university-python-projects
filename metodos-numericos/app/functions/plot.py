import matplotlib.pyplot as plt
import numpy as np
from io import BytesIO
import base64

def create_plot(a, b, func, function_expression):
    x_vals = np.linspace(a, b, 400)
    vectorized_func = np.vectorize(func)
    y_vals = vectorized_func(x_vals)

    plt.switch_backend('Agg')
    plt.figure(figsize=(8, 6))
    plt.plot(x_vals, y_vals, label=function_expression)
    plt.axhline(y=0, color='black', linewidth=0.8, linestyle='--')

    plt.plot(2.0, func(2.0), 'ro', label=f"Raíz aproximada: {2.0}")
        
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

