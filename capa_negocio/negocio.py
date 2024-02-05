# En capa_negocio/negocio.py
from datetime import datetime
from capa_datos.pacientes_db import PacientesDB


class Negocio:
    def __init__(self):
        self.db = PacientesDB()
        self.db.inicializar_base_datos()

    def agregar_paciente(self, nombre, tratamiento):
        fecha_ingreso = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.db.agregar_paciente(nombre, tratamiento, fecha_ingreso)

    def obtener_pacientes(self):
        return self.db.obtener_pacientes()

    def cerrar_conexion(self):
        self.db.cerrar_conexion()
