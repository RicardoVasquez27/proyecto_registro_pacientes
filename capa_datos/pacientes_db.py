# En capa_datos/pacientes_db.py
import sqlite3

class PacientesDB:
    def __init__(self, db_name='registro_pacientes.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def inicializar_base_datos(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS pacientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                tratamiento TEXT,
                fecha_ingreso DATE
            )
        ''')
        self.conn.commit()

    def agregar_paciente(self, nombre, tratamiento, fecha_ingreso):
        self.cursor.execute('''
            INSERT INTO pacientes (nombre, tratamiento, fecha_ingreso)
            VALUES (?, ?, ?)
        ''', (nombre, tratamiento, fecha_ingreso))
        self.conn.commit()

    def obtener_pacientes(self):
        self.cursor.execute('SELECT * FROM pacientes')
        return self.cursor.fetchall()

    def cerrar_conexion(self):
        self.conn.close()
