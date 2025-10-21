# main.py
from semaforo import SemaforoInteligente

def main():
    sistema = SemaforoInteligente()
    print("=== Simulación de Semáforo Inteligente ===")

    while True:
        try:
            flujo_a = int(input("Ingrese número de autos en vía A: "))
            flujo_b = int(input("Ingrese número de autos en vía B: "))

            tiempo_a, tiempo_b = sistema.calcular_tiempos(flujo_a, flujo_b)
            print(f"\nTiempo en verde - Vía A: {tiempo_a} s | Vía B: {tiempo_b} s\n")

            continuar = input("¿Desea ingresar otro flujo? (s/n): ").lower()
            if continuar != "s":
                sistema.guardar_datos()
                print("Datos guardados en datos.json")
                break

        except ValueError:
            print("Por favor, ingrese solo números enteros.")

if __name__ == "__main__":
    main()