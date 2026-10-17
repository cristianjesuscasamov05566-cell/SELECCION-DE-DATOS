import sqlite3

BASE_DATOS = "EMPLEADOS.db"


def crear_base_datos():
    conexion = sqlite3.connect(BASE_DATOS)

    conexion.execute("""
        CREATE TABLE IF NOT EXISTS empleados (
            CURP TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            calle TEXT NOT NULL,
            colonia TEXT NOT NULL,
            telefono TEXT NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()
    print("Base de datos EMPLEADOS creada correctamente.")


def alta_empleado():
    print("\n--- ALTA DE EMPLEADOS ---")

    curp = input("CURP: ").strip().upper()
    nombre = input("Nombre: ").strip()
    apellido = input("Apellido: ").strip()
    calle = input("Calle: ").strip()
    colonia = input("Colonia: ").strip()
    telefono = input("Telefono: ").strip()

    if not all([curp, nombre, apellido, calle, colonia, telefono]):
        print("Error: todos los campos son obligatorios.")
        return

    conexion = sqlite3.connect(BASE_DATOS)

    try:
        conexion.execute("""
            INSERT INTO empleados
            (CURP, nombre, apellido, calle, colonia, telefono)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (curp, nombre, apellido, calle, colonia, telefono))

        conexion.commit()
        print("Empleado registrado correctamente.")

    except sqlite3.IntegrityError:
        print("Error: la CURP ya existe.")

    finally:
        conexion.close()


def mostrar_empleados():
    conexion = sqlite3.connect(BASE_DATOS)

    cursor = conexion.execute("""
        SELECT CURP, nombre, apellido, calle, colonia, telefono
        FROM empleados
    """)

    empleados = cursor.fetchall()
    conexion.close()

    print("\n--- EMPLEADOS REGISTRADOS ---")

    if not empleados:
        print("No hay empleados registrados.")
        return

    for empleado in empleados:
        print("------------------------------")
        print("CURP:", empleado[0])
        print("Nombre:", empleado[1])
        print("Apellido:", empleado[2])
        print("Calle:", empleado[3])
        print("Colonia:", empleado[4])
        print("Telefono:", empleado[5])


def menu():
    crear_base_datos()

    while True:
        print("\n===== ACME S.A. DE C.V. =====")
        print("1. Crear base de datos")
        print("2. Dar de alta empleado")
        print("3. Mostrar empleados")
        print("4. Salir")

        opcion = input("Selecciona una opcion: ")

        if opcion == "1":
            crear_base_datos()
        elif opcion == "2":
            alta_empleado()
        elif opcion == "3":
            mostrar_empleados()
        elif opcion == "4":
            print("Hasta luego.")
            break
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()

