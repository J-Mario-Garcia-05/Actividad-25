import sqlite3

DB_NAME = "actividad_25.db"


class Estudiante:
    def __init__(self, nombre, carrera, promedio):
        self.nombre = nombre
        self.carrera = carrera
        self.promedio = promedio

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS estudiantes(
                id_estudiante INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                carrera TEXT NOT NULL,
                promedio REAL
            )
         """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO estudiantes (nombre, carrera, promedio) VALUES (?, ?, ?)",
                (self.nombre, self.carrera, self.promedio)
            )
        print(f"Estudiante '{self.nombre}' registrado con éxito.")

    @staticmethod
    def listar():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes")
            filas = cur.fetchall()
            if not filas:
                print("No hay estudiantes registrados.")
                return
            print("\n--- LISTADO DE ESTUDIANTES ---")
            for f in filas:
                print(
                    f"ID: {f['id_estudiante']} | Nombre: {f['nombre']} | Carrera: {f['carrera']} | Promedio: {f['promedio']}")

    @staticmethod
    def modificar():
        ide = input("Ingrese ID del estudiante a modificar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT * FROM estudiantes WHERE id_estudiante = ?", (ide,))
            fila = cur.fetchone()
            if not fila:
                print("No se encontró el estudiante.")
                return
            nombre = input(f"Nuevo nombre [{fila['nombre']}]: ") or fila['nombre']
            carrera = input(f"Nueva carrera [{fila['carrera']}]: ") or fila['carrera']
            promedio = input(f"Nuevo promedio [{fila['promedio']}]: ") or fila['promedio']
            conn.execute("UPDATE estudiantes SET nombre=?, carrera=?, promedio=? WHERE id_estudiante=?",
                         (nombre, carrera, promedio, ide))
        print("Estudiante actualizado con éxito.")

    @staticmethod
    def eliminar():
        ide = input("Ingrese ID del estudiante a eliminar: ")
        with Estudiante._conn() as conn:
            cur = conn.execute("DELETE FROM estudiantes WHERE id_estudiante = ?", (ide,))
            if cur.rowcount == 0:
                print("No se encontró el estudiante.")
            else:
                print("Estudiante eliminado con éxito.")

    @staticmethod
    def promedio_general():
        with Estudiante._conn() as conn:
            cur = conn.execute("SELECT AVG(promedio) AS prom FROM estudiantes")
            prom = cur.fetchone()["prom"]
            if prom:
                print(f"\nPromedio general: {prom:.2f}")
            else:
                print("No hay datos para calcular el promedio.")



class Cursos:
    def __init__(self, nombre):
        self.nombre = nombre

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS cursos(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO cursos (nombre) VALUES (?)",
                (self.nombre,)
            )
            print(f"Curso {self.nombre} registrado correctamente.")

    @staticmethod
    def listar():
        with Cursos._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos")
            lista = cur.fetchall()
            if not lista:
                print("No hay cursos registrados.")
                return
            print("\n--- LISTADO DE CURSOS ---")
            for curso in lista:
                print(f"Id: {curso['id']} | Nombre: {curso['nombre']}")

    @staticmethod
    def modificar():
        id = input("Ingrese ID del curso a modificar: ")
        with Cursos._conn() as conn:
            cur = conn.execute("SELECT * FROM cursos WHERE id = ?", (id,))
            curso = cur.fetchone()
            if not curso:
                print("No se encontró el curso")
                return
            nombre = input(f"Nuevo nombre [{curso['nombre']}]: ") or curso['nombre']
            conn.execute(
                "UPDATE cursos SET nombre=? WHERE id=?",
                (nombre, id)
            )
            print("Curso actualizado correctamente.")

    @staticmethod
    def eliminar():
        id = input("Ingrese ID del curso a eliminar: ")
        with Cursos._conn() as conn:
            cur = conn.execute("DELETE FROM cursos WHERE id = ?", (id,))
            if cur.rowcount == 0:
                print("No se encontró el curso.")
            else:
                print("Curso eliminado correctamente.")


class Docentes:
    def __init__(self, nombre, grado_academico, curso, salario):
        self.nombre = nombre
        self.grado_academico = grado_academico
        self.curso = curso
        self.salario = salario

    @staticmethod
    def _conn():
        conn = sqlite3.connect(DB_NAME)
        conn.row_factory = sqlite3.Row
        conn.execute("""
            CREATE TABLE IF NOT EXISTS docentes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nombre TEXT NOT NULL,
                grado_academico TEXT NOT NULL,
                curso INTEGER NOT NULL,
                salario REAL
            );
        """)
        conn.commit()
        return conn

    def guardar(self):
        with self._conn() as conn:
            conn.execute(
                "INSERT INTO docentes (nombre, grado_academico, curso, salario) VALUES(?, ?, ?, ?)",
                (self.nombre, self.grado_academico, self.curso, self.salario)
            )
            print(f"Docente {self.nombre} guardado correctamente.")

    @staticmethod
    def listar():
        with Docentes._conn() as conn:
            cur = conn.execute("SELECT * FROM docentes")
            docentes = cur.fetchall()
            if not docentes:
                print("No hay docentes registrados")
                return
            print("\n--LISTADO DE DOCENTES--")
            for docente in docentes:
                print(f"ID: {docente['id']} | Nombre: {docente['nombre']} | Grado Académico: {docente['grado_academico']}"
                      f"Curso: {docente['curso']} | Salario: {docente['salario']:.2f}")

    @staticmethod
    def modificar():
        id = input("Ingrese ID del docente a modificar: ")
        with Docentes._conn() as conn:
            cur = conn.execute("SELECT * FROM docentes WHERE id = ?", (id,))
            docente = cur.fetchone()
            if not docente:
                print("No se encontró al docente.")
                return
            nombre = input(f"Nuevo nombre |{docente['nombre']}|: ") or docente['nombre']
            grado_academico = input(f"Nuevo Grado académico |{docente['grado_academico']}|: ") or docente['grado_academico']
            curso = input(f"Id de Nuevo curso |{docente['curso']}|: ") or docente['curso']
            salario = input(f"Nuevo salario |{docente['salario']}|: ") or docente['salario']
            conn.execute(
                "UPDATE docentes SET nombre=?, grado_academico=?, curso=?, salario=? WHERE id=?",
                (nombre, grado_academico, curso, salario, id)
            )
            print("Datos del docente actualizado correctamente.")

    @staticmethod
    def eliminar():
        with Docentes._conn() as conn:
            id = input("Ingrese ID del docente a eliminar: ")
            cur = conn.execute("DELETE FROM docentes WHERE id_docente = ?", (id,))
            if cur.rowcount == 0:
                print("No se encontró al docente.")
            else:
                print("Docente eliminado correctamente.")

# --- MENÚ PRINCIPAL ---
def menu():
    while True:
        print("\n===== MENÚ DE ESTUDIANTES =====")
        print("1. Realizar registros")
        print("2. Listar tablas")
        print("3. Realizar modificaciones")
        print("4. Realizar eliminaciones")
        print("5. Promedio general de estudiantes")
        print("0. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            print("--Estudiante--")
            nombre = input("Nombre: ")
            carrera = input("Carrera: ")
            promedio = float(input("Promedio: "))
            e = Estudiante(nombre, carrera, promedio)
            e.guardar()
            print("\n--Docente--")
            nombre = input("Nombre: ")
            grado_academico = input("Grado academico: ")
            curso = input("Id de curso: ")
            salario = float(input("Salario: Q."))
            d = Docentes(nombre, grado_academico, curso, salario)
            d.guardar()
            print("\n--Curso--")
            nombre = input("Nombre: ")
            c = Cursos(nombre)
            c.guardar()
        elif opcion == "2":
            print("--ESTUDIANTES--")
            Estudiante.listar()
            print("\n--DOCENTES--")
            Docentes.listar()
            print("\n--CURSOS--")
            Cursos.listar()
        elif opcion == "3":
            print("--MODIFICAR ESTUDIANTES--")
            Estudiante.modificar()
            print("\n--MODIFICAR DOCENTES--")
            Docentes.modificar()
            print("\n--MODIFICAR CURSOS--")
            Cursos.modificar()
        elif opcion == "4":
            print("--ELIMINAR ESTUDIANTE--")
            Estudiante.eliminar()
            print("\n--ELIMINAR DOCENTE--")
            Docentes.eliminar()
            print("\n--ELIMINAR CURSO--")
            Cursos.eliminar()
        elif opcion == "5":
            Estudiante.promedio_general()
        elif opcion == "0":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    menu()
