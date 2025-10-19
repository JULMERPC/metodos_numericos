import numpy as np
from scipy.optimize import minimize_scalar

def optimizacion_unidimensional(expr, a, b):
    """Optimización unidimensional en el intervalo [a, b]."""
    try:
        f = lambda x: eval(expr, {"x": x, "np": np})
        res = minimize_scalar(f, bounds=(a, b), method='bounded')
        print(f"\nResultado: f(x) mínima = {res.fun:.4f} en x = {res.x:.4f}")
    except Exception as e:
        print("Error en el cálculo:", e)
