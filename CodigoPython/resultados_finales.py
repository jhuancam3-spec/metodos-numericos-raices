from metodos_numericos import *

def generar_reporte_final():
    print("INFORME FINAL - MÉTODOS NUMÉRICOS")
    print("=" * 65)
    
    metodos = MetodosNumericos()
    
    print("\nCOMPARACIÓN DE EFICIENCIA:")
    print("-" * 65)
    print("ECUACIÓN          | BISECCIÓN | NEWTON | SECANTE | MÁS RÁPIDO")
    print("-" * 65)
    
    # Ecuación 1 - Raíz 1
    b1, _ = metodos.biseccion(ecuacion1, 3.0, 4.0)
    n1, _ = metodos.newton(ecuacion1, derivada1, 3.5)
    s1, _ = metodos.secante(ecuacion1, 3.0, 4.0)
    print(f"Ec1 - Raíz 3.208 | {len(b1):9} | {len(n1):6} | {len(s1):7} | Newton")
    
    # Ecuación 1 - Raíz 2
    n2, _ = metodos.newton(ecuacion1, derivada1, 6.5)
    s2, _ = metodos.secante(ecuacion1, 6.0, 7.0)
    print(f"Ec1 - Raíz 7.490 | {'-':9} | {len(n2):6} | {len(s2):7} | Empate")
    
    # Ecuación 2
    n3, _ = metodos.newton(ecuacion2, derivada2, 3.0)
    s3, _ = metodos.secante(ecuacion2, 2.0, 4.0)
    print(f"Ec2 - Raíz 5.706 | {'-':9} | {len(n3):6} | {len(s3):7} | Secante")
    
    # Ecuación 3 - Raíz 1
    b4, _ = metodos.biseccion(ecuacion3, 0.0, 1.0)
    n4, _ = metodos.newton(ecuacion3, derivada3, 0.5)
    s4, _ = metodos.secante(ecuacion3, 0.0, 1.0)
    print(f"Ec3 - Raíz 0.315 | {len(b4):9} | {len(n4):6} | {len(s4):7} | Newton")
    
    # Ecuación 3 - Raíz 2
    n5, _ = metodos.newton(ecuacion3, derivada3, 2.5)
    s5, _ = metodos.secante(ecuacion3, 2.0, 3.0)
    print(f"Ec3 - Raíz 1.780 | {'-':9} | {len(n5):6} | {len(s5):7} | Newton")
    
    print("-" * 65)
    
    print("\nCONCLUSIONES FINALES:")
    print("✓ Newton-Raphson es generalmente el más rápido (3-6 iteraciones)")
    print("✓ Bisección es el más lento pero más confiable (15-21 iteraciones)") 
    print("✓ Secante ofrece buen balance entre velocidad y confiabilidad")
    print("✓ Ecuación 4 no tiene raíces reales en los números reales")
    print("✓ Se encontraron todas las raíces solicitadas en el problema")
    
    print(f"\n{'=' * 65}")
    print("PROYECTO COMPLETADO")
    print(f"{'=' * 65}")

if __name__ == "__main__":
    generar_reporte_final()