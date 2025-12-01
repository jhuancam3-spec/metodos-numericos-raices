import numpy as np
import matplotlib.pyplot as plt
import time

# ECUACIONES EXACTAS DEL PROBLEMA ORIGINAL
def f1(x):
    """x³ - e⁰·⁸ˣ = 20"""
    return x**3 - np.exp(0.8*x) - 20

def f2(x):
    """3·sin(0.5x) - 0.5x + 2 = 0"""
    return 3*np.sin(0.5*x) - 0.5*x + 2

def f3(x):
    """x³ - x²e⁻⁰·⁵ˣ - 3x = -1"""
    return x**3 - x**2*np.exp(-0.5*x) - 3*x + 1

def f4(x):
    """cos²x - 0.5xe⁰·³ˣ + 5 = 0"""
    return np.cos(x)**2 - 0.5*x*np.exp(0.3*x) + 5

# MÉTODO DE BISECCIÓN SIMPLE
def biseccion(f, a, b, tol=1e-6, max_iter=100):
    resultados = []
    for i in range(max_iter):
        c = (a + b) / 2
        fc = f(c)
        error = abs(b - a)
        
        resultados.append([i, a, b, c, fc, error])
        
        if abs(fc) < tol or error < tol:
            break
            
        if f(a) * fc < 0:
            b = c
        else:
            a = c
            
    return resultados

# GENERAR SOLO 4 GRÁFICAS CORRECTAS
def graficar_4_ecuaciones():
    plt.figure(figsize=(12, 8))
    
    # Configuración para cada subplot
    ecuaciones = [f1, f2, f3, f4]
    titulos = [
        'ECUACIÓN 1: $x^3 - e^{0.8x} = 20$',
        'ECUACIÓN 2: $3\\sin(0.5x) - 0.5x + 2 = 0$', 
        'ECUACIÓN 3: $x^3 - x^2e^{-0.5x} - 3x = -1$',
        'ECUACIÓN 4: $\\cos^2x - 0.5xe^{0.3x} + 5 = 0$'
    ]
    
    x_ranges = [(0, 8), (0, 8), (-2, 4), (-5, 5)]
    colors = ['blue', 'green', 'red', 'purple']
    
    for i in range(4):
        plt.subplot(2, 2, i+1)
        
        x = np.linspace(x_ranges[i][0], x_ranges[i][1], 1000)
        y = ecuaciones[i](x)
        
        plt.plot(x, y, color=colors[i], linewidth=2)
        plt.axhline(y=0, color='black', linestyle='--', alpha=0.5)
        plt.title(titulos[i], fontsize=10, fontweight='bold')
        plt.grid(True, alpha=0.3)
        plt.xlabel('x')
        plt.ylabel('f(x)')
        
        # Encontrar raíces aproximadas
        sign_changes = np.where(np.diff(np.sign(y)))[0]
        for idx in sign_changes:
            if idx < len(x) - 1:
                root_approx = x[idx]
                plt.plot(root_approx, 0, 'ro', markersize=6)
                plt.annotate(f'x≈{root_approx:.2f}', 
                           (root_approx, 0), 
                           xytext=(5, 15), 
                           textcoords='offset points',
                           fontsize=8,
                           bbox=dict(boxstyle="round,pad=0.2", facecolor="yellow", alpha=0.7))
    
    plt.tight_layout()
    plt.savefig('GRAFICAS_4_ECUACIONES.png', dpi=300, bbox_inches='tight')
    plt.show()

# ANÁLISIS NUMÉRICO SIMPLE
def analisis_numerico():
    print("ANÁLISIS NUMÉRICO DE LAS 4 ECUACIONES")
    print("=" * 50)
    
    # Configuración para cada ecuación
    configs = [
        {'nombre': 'Ecuación 1', 'func': f1, 'intervalos': [(3, 4), (6, 7)]},
        {'nombre': 'Ecuación 2', 'func': f2, 'intervalos': [(2, 4)]},
        {'nombre': 'Ecuación 3', 'func': f3, 'intervalos': [(-1, 0), (0, 1), (2, 3)]},
        {'nombre': 'Ecuación 4', 'func': f4, 'intervalos': [(-2, 2)]}
    ]
    
    for config in configs:
        print(f"\n{config['nombre']}:")
        for i, (a, b) in enumerate(config['intervalos']):
            resultados = biseccion(config['func'], a, b)
            if resultados:
                raiz = resultados[-1][3]
                iteraciones = len(resultados)
                print(f"  Raíz {i+1}: {raiz:.6f} (Iteraciones: {iteraciones})")

def main():
    print("SOLUCIÓN COMPLETA DEL PROBLEMA DE RAÍCES")
    print("4 ECUACIONES ORIGINALES:")
    print("1. x³ - e⁰·⁸ˣ = 20")
    print("2. 3·sin(0.5x) - 0.5x + 2 = 0") 
    print("3. x³ - x²e⁻⁰·⁵ˣ - 3x = -1")
    print("4. cos²x - 0.5xe⁰·³ˣ + 5 = 0")
    print("\n" + "="*50)
    
    # Paso 1: Generar gráficas
    print("\nPASO 1: Generando gráficas de las 4 ecuaciones...")
    graficar_4_ecuaciones()
    
    # Paso 2: Análisis numérico
    print("\nPASO 2: Realizando análisis numérico...")
    analisis_numerico()
    
    print("\n" + "="*50)
    print(" ANÁLISIS COMPLETADO")
    print(" Se generó: GRAFICAS_4_ECUACIONES.png")
    print(" Resultados numéricos listos para el reporte")

if __name__ == "__main__":
    main()