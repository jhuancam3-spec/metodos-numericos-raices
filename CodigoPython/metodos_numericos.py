import numpy as np
import matplotlib.pyplot as plt

class MetodosNumericos:
    def __init__(self, tol=1e-6, max_iter=100):
        self.tol = tol
        self.max_iter = max_iter
    
    def biseccion(self, f, a, b):
        """Método de bisección para encontrar raíces"""
        if f(a) * f(b) >= 0:
            return None, "No hay cambio de signo"
        
        resultados = []
        for i in range(self.max_iter):
            c = (a + b) / 2
            fc = f(c)
            error = abs(b - a)
            resultados.append([i, a, b, c, fc, error])
            
            if abs(fc) < self.tol or error < self.tol:
                break
            if f(a) * fc < 0:
                b = c
            else:
                a = c
        return resultados, "Convergido"
    
    def newton(self, f, df, x0):
        """Método de Newton-Raphson"""
        resultados = []
        x = x0
        for i in range(self.max_iter):
            fx = f(x)
            dfx = df(x)
            if abs(dfx) < 1e-12:
                return None, "Derivada cero"
            
            x_new = x - fx / dfx
            error = abs(x_new - x)
            resultados.append([i, x, fx, dfx, x_new, error])
            
            if abs(fx) < self.tol or error < self.tol:
                break
            x = x_new
        return resultados, "Convergido"
    
    def secante(self, f, x0, x1):
        """Método de la secante"""
        resultados = []
        x_prev, x_curr = x0, x1
        for i in range(self.max_iter):
            f_prev = f(x_prev)
            f_curr = f(x_curr)
            
            if abs(f_curr - f_prev) < 1e-12:
                return None, "División por cero"
            
            x_new = x_curr - f_curr * (x_curr - x_prev) / (f_curr - f_prev)
            error = abs(x_new - x_curr)
            resultados.append([i, x_prev, x_curr, x_new, f_curr, error])
            
            if abs(f_curr) < self.tol or error < self.tol:
                break
            x_prev, x_curr = x_curr, x_new
        return resultados, "Convergido"

# DEFINICIÓN DE LAS ECUACIONES
def ecuacion1(x):
    return x**3 - np.exp(0.8*x) - 20

def derivada1(x):
    return 3*x**2 - 0.8*np.exp(0.8*x)

def ecuacion2(x):
    return 3*np.sin(0.5*x) - 0.5*x + 2

def derivada2(x):
    return 1.5*np.cos(0.5*x) - 0.5

def ecuacion3(x):
    return x**3 - x**2*np.exp(-0.5*x) - 3*x + 1

def derivada3(x):
    return 3*x**2 - 2*x*np.exp(-0.5*x) + 0.5*x**2*np.exp(-0.5*x) - 3

def ecuacion4(x):
    return np.cos(x)**2 - 0.5*x*np.exp(0.3*x) + 5

def derivada4(x):
    return -2*np.cos(x)*np.sin(x) - 0.5*np.exp(0.3*x) - 0.15*x*np.exp(0.3*x)