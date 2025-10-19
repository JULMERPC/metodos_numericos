import numpy as np
from scipy.optimize import minimize

def optimizacion_con_restricciones(expr, restr, x0):
    """Optimización con una restricción de igualdad."""
    try:
        f = lambda x: eval(expr, {"x": x[0], "y": x[1], "np": np})
        cons = {'type': 'eq', 'fun': lambda x: eval(restr, {"x": x[0], "y": x[1], "np": np})}
        res = minimize(f, x0, constraints=cons, method='SLSQP')
        print(f"\nResultado: f(x,y) mínima = {res.fun:.4f} en punto {res.x}")
    except Exception as e:
        print("Error en el cálculo:", e)
