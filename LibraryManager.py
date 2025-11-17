"""
Proyecto Práctico Integrador
Aplicación de Consola: Sistema de Gestión de Biblioteca

Descripción General:
Este programa permite administrar una biblioteca básica desde consola.
El usuario podrá registrar libros, gestionarlos, realizar préstamos,
devolver libros, consultar información y ver estadísticas generales.

Funcionalidades Requeridas:

1. Registrar un libro:
   - Campos: título, autor, año, ISBN, categoría y estado.
   - Validaciones: título no vacío, ISBN único, año válido.
   - Estado inicial del libro: "Disponible".

2. Mostrar todos los libros:
   - Lista completa ordenada alfabéticamente por título.
   - Mostrar título, autor, año, ISBN, categoría y estado.

3. Buscar libros:
   - Búsqueda flexible por título, autor o categoría.
   - No sensible a mayúsculas/minúsculas.

4. Registrar un préstamo:
   - Seleccionar un libro disponible.
   - Registrar nombre de la persona y fecha del préstamo.
   - Cambiar estado del libro a "Prestado".
   - Validar que el libro no esté ya prestado.

5. Registrar la devolución de un libro:
   - Mostrar libros prestados.
   - Seleccionar cuál se devuelve.
   - Registrar fecha de devolución.
   - Cambiar estado del libro a "Disponible".

6. Mostrar historial de préstamos:
   - Listar todos los préstamos realizados.
   - Mostrar fechas, estado actual y persona que lo tomó.

7. Estadísticas de la biblioteca:
   - Total de libros.
   - Libros disponibles.
   - Libros prestados.
   - Libro más prestado.
   - Categoría más común.

8. Eliminar libro:
   - Mostrar lista numerada de libros.
   - Confirmar antes de borrar.
   - No permitir eliminar libros prestados.

9. Salir del sistema:
   - Mostrar mensaje de despedida.
"""

#Listas
libros = []
prestamos = []

#Funciones

def registrar_libro():
    print("\n--- Registrar libros ---")
    
    titulo = input("Ingrese el titulo del libro: ").strip().lower()
    autor = input("Ingrese el nombre del autor del libro: ").strip().lower()
    anio = int(input("Ingrese el año de publicacion: "))
    while True: # Validar ISBN único
        try:
            isbn = int(input("Ingrese un ISBN único: "))
        except ValueError:
            print("Error: el ISBN debe ser un número.")
            continue
        isbn_existente = any(libro["isbn"] == isbn for libro in libros)
        if isbn_existente:
            print("Ese ISBN ya está registrado. Ingrese otro.")
        else:
            break
    categoria = input("Ingrese la categoria correspondiente: ").strip().lower()
    estado = True  
    
    libro = {"titulo": titulo, "autor": autor, "anio": anio, "isbn": isbn, "categoria": categoria, "estado": estado}
    libros.append(libro)   
    print(f"El libro '{titulo}' ha sido registrado exitosamente.")
    
def mostrar_libros():
    print("\n--- Lista de libros registrados ---")
    
    if not libros:
        print("No hay libros registrados.")
        return
    libros_ordenados = sorted(libros, key=lambda x: x["titulo"])
    for libro in libros_ordenados:
        estado_str = "Disponible" if libro["estado"] else "Prestado"
        print(f"Título: {libro['titulo'].title()}, Autor: {libro['autor'].title()}, Año: {libro['anio']}, ISBN: {libro['isbn']}, Categoría: {libro['categoria'].title()}, Estado: {estado_str}")

def buscar_libro():
      print("\n--- Buscar libro registrado ---")
      
      opcion = int(input("Ingrese 1 para bucar por nombre.\nIngrese 2 para buscar por autor.\nIngrese 3 para buscar por categoria.\nSu opcion es: "))
      
      if opcion == 1:
         busqueda = input("Escribe el titulo que quieres buscar: ")
         encontrados = [e for e in libros if busqueda in e["titulo"].lower()]
         
         if encontrados:
            for e in encontrados:
               print(f"{e['titulo']} - {e['autor']} - {e['anio']} - {e['isbn']} - {e['categoria']} - {'Disponible' if e['estado'] else 'Prestado'}")
         else:
            print("No se encontro ningun libro")
      elif opcion == 2:
         busqueda = input("Escribe el autor que desea buscar: ")
         encontrados = [e for e in libros if busqueda in e["autor"].lower()]
         
         if encontrados:
            for e in encontrados:
               print(f"{e['titulo']} - {e['autor']} - {e['anio']} - {e['isbn']} - {e['categoria']} - {'Disponible' if e['estado'] else 'Prestado'}")
         else:
            print("No se encontro ningun libro")
      elif opcion == 3:
         busqueda = input("Escribe la categoria que desea buscar: ")
         encontrados = [e for e in libros if busqueda in e["categoria"].lower()]
         
         if encontrados:
            for e in encontrados:
               print(f"{e['titulo']} - {e['autor']} - {e['anio']} - {e['isbn']} - {e['categoria']} - {'Disponible' if e['estado'] else 'Prestado'}")
         else:
            print("No se encontro ningun libro")
      else:
         print("Opcion invalida")
     
def registrar_prestamo():
      print("\n--- Registrar préstamo de libro ---")
      
      libros_disponibles = [libro for libro in libros if libro["estado"]]
      
      if not libros_disponibles:
         print("No hay libros disponibles para préstamo.")
         return
      print("Libros disponibles:")
      for idx, libro in enumerate(libros_disponibles, start=1):
         print(f"{idx}. {libro['titulo'].title()} (ISBN: {libro['isbn']})")
      seleccion = int(input("Seleccione el número del libro a prestar: ")) - 1
      if seleccion < 0 or seleccion >= len(libros_disponibles):
         print("Selección inválida.")
         return
      
      libro_seleccionado = libros_disponibles[seleccion]
      nombre_persona = input("Ingrese el nombre de la persona que toma el préstamo: ").strip()
      fecha_prestamo = input("Ingrese la fecha del préstamo (DD/MM/AAAA): ").strip()
      
      libro_seleccionado["estado"] = False  
      prestamo = {"isbn": libro_seleccionado["isbn"], "nombre_persona": nombre_persona, "fecha_prestamo": fecha_prestamo, "fecha_devolucion": None}
      prestamos.append(prestamo)
      print(f"El libro '{libro_seleccionado['titulo'].title()}' ha sido prestado a {nombre_persona}.")
      
def registrar_devolucion():
      print("\n--- Registrar devolución de libro ---")
      
      libros_prestados = [libro for libro in libros if not libro["estado"]]
      
      if not libros_prestados:
         print("No hay libros prestados para devolver.")
         return
      print("Libros prestados:")
      for idx, libro in enumerate(libros_prestados, start=1):
         print(f"{idx}. {libro['titulo'].title()} (ISBN: {libro['isbn']})")
      seleccion = int(input("Seleccione el número del libro a devolver: ")) - 1
      if seleccion < 0 or seleccion >= len(libros_prestados):
         print("Selección inválida.")
         return
      
      libro_seleccionado = libros_prestados[seleccion]
      fecha_devolucion = input("Ingrese la fecha de devolución (DD/MM/AAAA): ").strip()
      
      libro_seleccionado["estado"] = True  
      for prestamo in prestamos:
         if prestamo["isbn"] == libro_seleccionado["isbn"] and prestamo["fecha_devolucion"] is None:
            prestamo["fecha_devolucion"] = fecha_devolucion
            break
      print(f"El libro '{libro_seleccionado['titulo'].title()}' ha sido devuelto.")
      
def mostrar_historial_prestamos():
      print("\n--- Historial de préstamos ---")
      
      if not prestamos:
         print("No hay registros de préstamos.")
         return
      for prestamo in prestamos:
         estado = "Devuelto" if prestamo["fecha_devolucion"] else "En préstamo"
         print(f"ISBN: {prestamo['isbn']}, Persona: {prestamo['nombre_persona']}, Fecha Préstamo: {prestamo['fecha_prestamo']}, Fecha Devolución: {prestamo['fecha_devolucion'] if prestamo['fecha_devolucion'] else 'N/A'}, Estado: {estado}")
         
def mostrar_estadisticas():
      print("\n--- Estadísticas de la biblioteca ---")
      
      total_libros = len(libros)
      libros_disponibles = sum(1 for libro in libros if libro["estado"])
      libros_prestados = total_libros - libros_disponibles
      porcentaje_disponibles = (libros_disponibles / total_libros) * 100 if total_libros > 0 else 0
      porcentaje_prestados = (libros_prestados / total_libros) * 100 if total_libros > 0 else 0
      
      print(f"Total de libros: {total_libros}")
      print(f"Hay {porcentaje_disponibles:.2f}% de libros disponibles: {libros_disponibles}")
      print(f"Hay {porcentaje_prestados:.2f}% de libros prestados: {libros_prestados}")
      
def eliminar_libro():
      print("\n--- Eliminar libro registrado ---")
      
      if not libros:
         print("No hay libros registrados para eliminar.")
         return
      print("Libros registrados:")
      for idx, libro in enumerate(libros, start=1):
         estado_str = "Disponible" if libro["estado"] else "Prestado"
         print(f"{idx}. {libro['titulo'].title()} (ISBN: {libro['isbn']}) - {estado_str}")
      seleccion = int(input("Seleccione el número del libro a eliminar: ")) - 1
      if seleccion < 0 or seleccion >= len(libros):
         print("Selección inválida.")
         return
      
      libro_seleccionado = libros[seleccion]
      if not libro_seleccionado["estado"]:
         print("No se puede eliminar un libro que está prestado.")
         return
      
      confirmacion = input(f"¿Está seguro de que desea eliminar el libro '{libro_seleccionado['titulo'].title()}'? (s/n): ").strip().lower()
      if confirmacion == 's':
         libros.remove(libro_seleccionado)
         print(f"El libro '{libro_seleccionado['titulo'].title()}' ha sido eliminado.")
      else:
         print("Eliminación cancelada.")
   
# Rellenar "base de datos" inicial de libros
libros = [
    {"titulo": "cien años de soledad", "autor": "gabriel garcia marquez", "anio": 1967, "isbn": 1001, "categoria": "novela", "estado": True},
    {"titulo": "el amor en los tiempos del cólera", "autor": "gabriel garcia marquez", "anio": 1985, "isbn": 1002, "categoria": "novela", "estado": True},
    {"titulo": "1984", "autor": "george orwell", "anio": 1949, "isbn": 1003, "categoria": "distopía", "estado": True},
    {"titulo": "rebelión en la granja", "autor": "george orwell", "anio": 1945, "isbn": 1004, "categoria": "satira", "estado": True},
    {"titulo": "don quijote de la mancha", "autor": "miguel de cervantes", "anio": 1605, "isbn": 1005, "categoria": "novela", "estado": True},
    {"titulo": "la odisea", "autor": "homero", "anio": -800, "isbn": 1006, "categoria": "epico", "estado": True},
    {"titulo": "la iliada", "autor": "homero", "anio": -750, "isbn": 1007, "categoria": "epico", "estado": True},
    {"titulo": "harry potter y la piedra filosofal", "autor": "j.k. rowling", "anio": 1997, "isbn": 1008, "categoria": "fantasia", "estado": True},
    {"titulo": "harry potter y la cámara secreta", "autor": "j.k. rowling", "anio": 1998, "isbn": 1009, "categoria": "fantasia", "estado": True},
    {"titulo": "harry potter y el prisionero de azkaban", "autor": "j.k. rowling", "anio": 1999, "isbn": 1010, "categoria": "fantasia", "estado": True},
    {"titulo": "el señor de los anillos: la comunidad del anillo", "autor": "j.r.r. tolkien", "anio": 1954, "isbn": 1101, "categoria": "fantasia", "estado": True},
    {"titulo": "el señor de los anillos: las dos torres", "autor": "j.r.r. tolkien", "anio": 1954, "isbn": 1102, "categoria": "fantasia", "estado": True},
    {"titulo": "el señor de los anillos: el retorno del rey", "autor": "j.r.r. tolkien", "anio": 1955, "isbn": 1103, "categoria": "fantasia", "estado": True},
    {"titulo": "el hobbit", "autor": "j.r.r. tolkien", "anio": 1937, "isbn": 1104, "categoria": "fantasia", "estado": True},
    {"titulo": "el principito", "autor": "antoine de saint-exupéry", "anio": 1943, "isbn": 1105, "categoria": "fantasia", "estado": True},
    {"titulo": "crimen y castigo", "autor": "fiódor dostoyevski", "anio": 1866, "isbn": 1106, "categoria": "novela", "estado": True},
    {"titulo": "los miserables", "autor": "victor hugo", "anio": 1862, "isbn": 1107, "categoria": "novela", "estado": True},
    {"titulo": "orgullo y prejuicio", "autor": "jane austen", "anio": 1813, "isbn": 1108, "categoria": "romance", "estado": True},
    {"titulo": "drácula", "autor": "bram stoker", "anio": 1897, "isbn": 1109, "categoria": "terror", "estado": True},
    {"titulo": "frankenstein", "autor": "mary shelley", "anio": 1818, "isbn": 1110, "categoria": "terror", "estado": True},
    {"titulo": "la metamorfosis", "autor": "franz kafka", "anio": 1915, "isbn": 1111, "categoria": "novela", "estado": True},
    {"titulo": "el alquimista", "autor": "paulo coelho", "anio": 1988, "isbn": 1112, "categoria": "ficcion", "estado": True},
    {"titulo": "sapiens: de animales a dioses", "autor": "yuval noah harari", "anio": 2011, "isbn": 1113, "categoria": "historia", "estado": True},
    {"titulo": "breves respuestas a las grandes preguntas", "autor": "stephen hawking", "anio": 2018, "isbn": 1114, "categoria": "ciencia", "estado": True},
    {"titulo": "cosmos", "autor": "carl sagan", "anio": 1980, "isbn": 1115, "categoria": "ciencia", "estado": True},
    {"titulo": "el código da vinci", "autor": "dan brown", "anio": 2003, "isbn": 1116, "categoria": "suspenso", "estado": True},
    {"titulo": "it", "autor": "stephen king", "anio": 1986, "isbn": 1117, "categoria": "terror", "estado": True},
    {"titulo": "el resplandor", "autor": "stephen king", "anio": 1977, "isbn": 1118, "categoria": "terror", "estado": True},
    {"titulo": "el arte de la guerra", "autor": "sun tzu", "anio": -500, "isbn": 1119, "categoria": "estrategia", "estado": True},
    {"titulo": "padre rico padre pobre", "autor": "robert kiyosaki", "anio": 1997, "isbn": 1120, "categoria": "finanzas", "estado": True}
]

def menu():
    while True:
        print("\n*** MENÚ PRINCIPAL ***")
        print("1. Registrar libro.")
        print("2. Mostrar todos los libros.")
        print("3. Buscar libro por título, autor, categoría o ISBN.")
        print("4. Registrar préstamo.")
        print("5. Registrar devolución.")
        print("6. Mostrar historial de préstamos.")
        print("7. Estadísticas de la biblioteca.")
        print("8. Eliminar libro.")
        print("9. Salir")
        
        opcion = input("Elija un opción (1-9): ")
        
        if opcion == "1":
            registrar_libro()
        elif opcion == "2":
            mostrar_libros()
        elif opcion == "3":
            buscar_libro()
        elif opcion == "4":
            registrar_prestamo()
        elif opcion == "5":
            registrar_devolucion()
        elif opcion == "6":
            mostrar_historial_prestamos()
        elif opcion == "7":
            mostrar_estadisticas()
        elif opcion == "8":
            eliminar_libro()
        elif opcion == "9":
            print("Muchas gracias por usar el sistema de gestión de biblioteca. ¡Hasta luego!")
            break
        else:
            print("Opción invalida, intente de nuevo..")

def main():
    menu()

if __name__ == "__main__":
    main()