#simulacro1.py
estudiantes = [
    {"id": "5001", "nombre": "luciana florez", "edad": "19", "notas": "3.5"},
    {"id": "5002", "nombre": "shamantha gomez", "edad": "20", "notas": "1.5" },
    {"id": "5003", "nombre": "neytan vasquez", "edad": "23", "notas": "2.5"},
    {"id": "5004", "nombre": "jeronimo avendaño", "edad": "21", "notas": "5.0"},
    {"id": "5005", "nombre": "emmanuel jaramillo", "edad": "16", "notas": "4.5"},
] 
def agregar_estudiantes():
    id_est = input("ingrese el id del estudiante: ")
    if any (e["id"] == id_est for e in estudiantes ) :
        print("ya existe un estudiante con ese id.")
        return 
    nombre = input("ingrese el nombre completo: ")
    try:    
        edad = int(input("ingrese la edad:"))

        notas = float(input("ingrese la nota (0.0 - 5.0) "))
    except ValueError:
        print("edad debe ser un numero enteron y un numero decimal.")
        return 
    if  edad <= 0:
        print("la edad debe ser positiva.")
        return 
    if not (0.0 <= notas <= 5.0):
        print("la nota debe estar entre 0.0 y 5.0.")
        return 
    estudiantes.append({"id": id_est, "nombre": nombre, "edad": edad, "notas": notas,})
    print("estudiante agregado correctamente.")

def buscar_por_id():
    id_est = input("ingresa el id del estudiante: ")
    for e in estudiantes: 
        if e ["id"] == id_est:
            print("estudiante encontrado:", e)
            return
        print("no se encontro un estudiante con ese id.")

def buscar_por_nombres():
    nombre = input("ingrese parte del nombre del estudiante: ").lower()
    encontrados = [e for e in estudiantes if nombre in e ["nombre"].lower()]
    if encontrados:
        for e in encontrados:
            print(e)
        else:
            print("no se encontro estudiante con ese nombre.")

def actualizar_estudiantes():
    id_est = input("ingresa el id del estudiante que deceas actualizar.")
    for e in estudiantes: 
        if e["id"] == id_est :
            edad_input = input("nueva edad (deje en blanco para no cambiar): ")
            notas_input = input("nueva notas(deje en blanco para no cambiar): ")
            if edad_input:
                try:
                    edad =int(edad_input)
                    if edad <= 0:
                        print("edad invalidad.")
                    e ["edad"] = edad 
                except ValueError:
                    print("edad invalidad.")
                    return
                if notas_input:
                    try:
                        notas = float(notas_input)
                        if not (0.0 <= notas <= 5.0):
                            print("nota invalidad.")
                            return
                        e ["notas"] = notas
                    except ValueError:
                        print("notas invalidad.")
                        return
                    print("estudiante actualizado correctamente.")
                    return
                print("no se encontro el estudiante")

def eliminar_estudiantes():
    id_est = input("ingrese el id del estudiante a eliminar: ")
    global estudiantes
    for e in  estudiantes:
        if e ["id"] == id_est:
            estudiantes = [est for est in estudiantes if est ["id"] != id_est]
            print("estudiante borrado correctamente. ")
            return
        print("no se encontro el estudiante.")

def calcular_promedio():
    if not estudiantes:
        print("no hay estudiantes registrados: ")
        return
    promedio = sum(e["notas"] for e in estudiantes) / len (estudiantes)
    print(f"promedio de notas: {promedio: .2f}")

def listar_bajo_umbral():
    try:
        umbral = float(input("ingrese el umbral de nota (por defecto 3.0): ") or 3.0)
    except ValueError:
        print("entrada invalidad")                 
        return 
    bajos = [e for e in estudiantes if e ["notas"] < umbral]
    if bajos:
        print(f"estudiante con notas menores a {umbral}:")
        for e in bajos:
            print(e)
        else:
            print("no hay estudiante de bajo de ese umbral.")



while True:
        print("\n--- MENÚ DE GESTIÓN DE ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Buscar por ID")
        print("3. Buscar por nombre")
        print("4. Actualizar estudiante")
        print("5. Eliminar estudiante")
        print("6. Calcular promedio de notas")
        print("7. Listar estudiantes con nota baja")
        print("8. Salir")
        opcion = input("Seleccione una opción (1-8): ")

        if opcion == "1":
            agregar_estudiantes()
        elif opcion == "2":
            buscar_por_id()
        elif opcion == "3":
            buscar_por_nombres()
        elif opcion == "4":
            actualizar_estudiantes()
        elif opcion == "5":
            eliminar_estudiantes()
        elif opcion == "6":
            calcular_promedio()
        elif opcion == "7":
            listar_bajo_umbral()
        elif opcion == "8":
            print("Saliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("Opción inválida. Intente de nuevo.")

                    



