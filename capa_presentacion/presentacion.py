# En capa_presentacion/presentacion.py
from capa_negocio.negocio import Negocio


class Presentacion:
    def __init__(self):
        self.negocio = Negocio()

    def menu_principal(self):
        while True:
            print("1. Agregar Paciente")
            print("2. Mostrar Pacientes")
            print("3. Salir")

            opcion = input("Selecciona una opción: ")

            if opcion == '1':
                nombre = input("Nombre del paciente: ")
                tratamiento = input("Tratamiento: ")
                self.negocio.agregar_paciente(nombre, tratamiento)
                print("Paciente agregado exitosamente.")
            elif opcion == '2':
                pacientes = self.negocio.obtener_pacientes()
                for paciente in pacientes:
                    print(paciente)
            elif opcion == '3':
                self.negocio.cerrar_conexion()
                break
            else:
                print("Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    presentacion = Presentacion()
    presentacion.menu_principal()
