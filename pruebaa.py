import json

class Libreria:
    def __init__(self):
        self.libros = []

    def anadir_libro(self, titulo, autor, genero, anio):
        if not titulo or not autor or not genero or not anio:
            return "Datos del libro incompletos"
        libro = {
            'titulo': titulo,
            'autor': autor,
            'genero': genero,
            'anio': anio
        }
        self.libros.append(libro)
        return "Libro añadido"

    def buscar_libro(self, titulo):
        return [libro for libro in self.libros if libro['titulo'] == titulo]

    def buscar_por_autor(self, autor):
        return [libro for libro in self.libros if libro['autor'] == autor]

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro['titulo'] == titulo:
                self.libros.remove(libro)
                return "Libro eliminado"
        return "Libro no encontrado"

    def guardar_libros(self, archivo):
        try:
            with open(archivo, 'w') as f:
                json.dump(self.libros, f)
            return "Libros guardados"
        except IOError:
            return "Error al guardar los libros"

    def cargar_libros(self, archivo):
        try:
            with open(archivo, 'r') as f:
                self.libros = json.load(f)
            return "Libros cargados"
        except FileNotFoundError:
            return "Archivo no encontrado"
        except json.JSONDecodeError:
            return "Error al cargar los libros"
