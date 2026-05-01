import requests

BASE_URL = 'http://127.0.0.1:5000'

def mostrar_menu():
    print("\n--- SISTEMA DE GESTIÓN DE TAREAS (CLIENTE) ---")
    print("1. Registrar un nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Ver mis tareas (HTML)")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Elegí una opción (1-4): ")

        if opcion == '1':
            usuario = input("Ingresá tu usuario: ")
            contrasena = input("Ingresá tu contraseña: ")
            payload = {"usuario": usuario, "contraseña": contrasena}
            respuesta = requests.post(f"{BASE_URL}/registro", json=payload)
            print(f"\nRespuesta del servidor ({respuesta.status_code}):", respuesta.text)

        elif opcion == '2':
            usuario = input("Ingresá tu usuario: ")
            contrasena = input("Ingresá tu contraseña: ")
            payload = {"usuario": usuario, "contraseña": contrasena}
            respuesta = requests.post(f"{BASE_URL}/login", json=payload)
            print(f"\nRespuesta del servidor ({respuesta.status_code}):", respuesta.text)

        elif opcion == '3':
            respuesta = requests.get(f"{BASE_URL}/tareas")
            print(f"\n--- HTML RECIBIDO ({respuesta.status_code}) ---")
            print(respuesta.text)

        elif opcion == '4':
            print("Cerrando el cliente...")
            break
        else:
            print("Opción no válida. Intentá de nuevo.")

if __name__ == '__main__':
    # Asegurarse de que el servidor.py esté corriendo en otra terminal antes de usar esto
    main()