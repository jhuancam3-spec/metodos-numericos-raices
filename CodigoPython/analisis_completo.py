from metodos_numericos import *

def main():
    print("ANÁLISIS NUMÉRICO COMPLETO - 3 MÉTODOS")
    print("=" * 60)
    
    metodos = MetodosNumericos(tol=1e-6, max_iter=100)
    
    # ECUACIÓN 1: x³ - e⁰·⁸ˣ = 20 (2 raíces)
    print("\nECUACIÓN 1: x³ - e⁰·⁸ˣ = 20")
    print("-" * 40)
    
    print("Raíz 1 (entre 3 y 4):")
    b1, _ = metodos.biseccion(ecuacion1, 3.0, 4.0)
    n1, _ = metodos.newton(ecuacion1, derivada1, 3.5)
    s1, _ = metodos.secante(ecuacion1, 3.0, 4.0)
    
    if b1: print(f"  Bisección: {b1[-1][3]:.6f} (iteraciones: {len(b1)})")
    if n1: print(f"  Newton:    {n1[-1][4]:.6f} (iteraciones: {len(n1)})")
    if s1: print(f"  Secante:   {s1[-1][3]:.6f} (iteraciones: {len(s1)})")
    
    print("\nRaíz 2 (entre 6 y 7):")
    b2, _ = metodos.biseccion(ecuacion1, 6.0, 7.0)
    n2, _ = metodos.newton(ecuacion1, derivada1, 6.5)
    s2, _ = metodos.secante(ecuacion1, 6.0, 7.0)
    
    if b2: print(f"  Bisección: {b2[-1][3]:.6f} (iteraciones: {len(b2)})")
    if n2: print(f"  Newton:    {n2[-1][4]:.6f} (iteraciones: {len(n2)})")
    if s2: print(f"  Secante:   {s2[-1][3]:.6f} (iteraciones: {len(s2)})")
    
    # ECUACIÓN 2: 3·sin(0.5x) - 0.5x + 2 = 0
    print("\nECUACIÓN 2: 3·sin(0.5x) - 0.5x + 2 = 0")
    print("-" * 40)
    
    b3, _ = metodos.biseccion(ecuacion2, 2.0, 4.0)
    n3, _ = metodos.newton(ecuacion2, derivada2, 3.0)
    s3, _ = metodos.secante(ecuacion2, 2.0, 4.0)
    
    if b3: print(f"  Bisección: {b3[-1][3]:.6f} (iteraciones: {len(b3)})")
    if n3: print(f"  Newton:    {n3[-1][4]:.6f} (iteraciones: {len(n3)})")
    if s3: print(f"  Secante:   {s3[-1][3]:.6f} (iteraciones: {len(s3)})")
    
    # ECUACIÓN 3: x³ - x²e⁻⁰·⁵ˣ - 3x = -1 (3 raíces)
    print("\nECUACIÓN 3: x³ - x²e⁻⁰·⁵ˣ - 3x = -1")
    print("-" * 40)
    
    print("Raíz 1 (entre -1 y 0):")
    b4, _ = metodos.biseccion(ecuacion3, -1.0, 0.0)
    n4, _ = metodos.newton(ecuacion3, derivada3, -0.5)
    s4, _ = metodos.secante(ecuacion3, -1.0, 0.0)
    
    if b4: print(f"  Bisección: {b4[-1][3]:.6f} (iteraciones: {len(b4)})")
    if n4: print(f"  Newton:    {n4[-1][4]:.6f} (iteraciones: {len(n4)})")
    if s4: print(f"  Secante:   {s4[-1][3]:.6f} (iteraciones: {len(s4)})")
    
    print("\nRaíz 2 (entre 0 y 1):")
    b5, _ = metodos.biseccion(ecuacion3, 0.0, 1.0)
    n5, _ = metodos.newton(ecuacion3, derivada3, 0.5)
    s5, _ = metodos.secante(ecuacion3, 0.0, 1.0)
    
    if b5: print(f"  Bisección: {b5[-1][3]:.6f} (iteraciones: {len(b5)})")
    if n5: print(f"  Newton:    {n5[-1][4]:.6f} (iteraciones: {len(n5)})")
    if s5: print(f"  Secante:   {s5[-1][3]:.6f} (iteraciones: {len(s5)})")
    
    print("\nRaíz 3 (entre 2 y 3):")
    b6, _ = metodos.biseccion(ecuacion3, 2.0, 3.0)
    n6, _ = metodos.newton(ecuacion3, derivada3, 2.5)
    s6, _ = metodos.secante(ecuacion3, 2.0, 3.0)
    
    if b6: print(f"  Bisección: {b6[-1][3]:.6f} (iteraciones: {len(b6)})")
    if n6: print(f"  Newton:    {n6[-1][4]:.6f} (iteraciones: {len(n6)})")
    if s6: print(f"  Secante:   {s6[-1][3]:.6f} (iteraciones: {len(s6)})")
    
    # ECUACIÓN 4: cos²x - 0.5xe⁰·³ˣ + 5 = 0
    print("\nECUACIÓN 4: cos²x - 0.5xe⁰·³ˣ + 5 = 0")
    print("-" * 40)
    print("ANÁLISIS: Esta ecuación probablemente no tiene raíces reales")
    print(f"f(0) = {ecuacion4(0):.2f}")
    print(f"f(5) = {ecuacion4(5):.2f}")
    print(f"f(-5) = {ecuacion4(-5):.2f}")
    
    print("\n" + "=" * 60)
    print(" ANÁLISIS COMPLETADO - LISTO PARA EL REPORTE")

if __name__ == "__main__":
    main()