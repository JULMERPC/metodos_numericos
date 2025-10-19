import numpy as np
from scipy.optimize import minimize

def optimizacion_multidimensional(expr, x0):
    """Optimización multidimensional sin restricciones."""
    try:
        f = lambda x: eval(expr, {"x": x[0], "y": x[1], "np": np})
        res = minimize(f, x0, method='BFGS')
        print(f"\nResultado: f(x,y) mínima = {res.fun:.4f} en punto {res.x}")
    except Exception as e:
        print("Error en el cálculo:", e)
