import unittest
import os
from pruebaa import Libreria

class TestLibreria(unittest.TestCase):
    
    def setUp(self):
        self.libreria = Libreria()
        self.libro = {
            'titulo': 'Cien años de soledad',
            'autor': 'Gabriel García Márquez',
            'genero': 'Novela',
            'anio': 1967
        }
    
    def tearDown(self):
        if os.path.exists("test_libreria.json"):
            os.remove("test_libreria.json")

    # Casos típicos
    def test_anadir_libro(self):
        mensaje = self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        self.assertEqual(mensaje, "Libro añadido")
        self.assertIn(self.libro, self.libreria.libros)

    # Caso extremo: Añadir un libro con datos faltantes
    def test_anadir_libro_datos_faltantes(self):
        mensaje = self.libreria.anadir_libro("", "", "", "")
        self.assertEqual(mensaje, "Datos del libro incompletos")

    # Casos típicos
    def test_buscar_libro(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        resultado = self.libreria.buscar_libro('Cien años de soledad')
        self.assertEqual(resultado, [self.libro])

    # Caso extremo: Buscar un libro que no existe
    def test_buscar_libro_no_existente(self):
        resultado = self.libreria.buscar_libro('Libro no existente')
        self.assertEqual(resultado, [])

    # Casos típicos
    def test_buscar_por_autor(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        resultado = self.libreria.buscar_por_autor('Gabriel García Márquez')
        self.assertEqual(resultado, [self.libro])

    # Caso extremo: Buscar por autor que no existe
    def test_buscar_por_autor_no_existente(self):
        resultado = self.libreria.buscar_por_autor('Autor Desconocido')
        self.assertEqual(resultado, [])

    # Casos típicos
    def test_eliminar_libro(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        mensaje = self.libreria.eliminar_libro('Cien años de soledad')
        self.assertEqual(mensaje, "Libro eliminado")
        self.assertNotIn(self.libro, self.libreria.libros)

    # Caso extremo: Eliminar un libro que no existe
    def test_eliminar_libro_no_existente(self):
        mensaje = self.libreria.eliminar_libro('Libro no existente')
        self.assertEqual(mensaje, "Libro no encontrado")

    # Casos típicos
    def test_guardar_libros(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        mensaje = self.libreria.guardar_libros("test_libreria.json")
        self.assertEqual(mensaje, "Libros guardados")
        self.assertTrue(os.path.exists("test_libreria.json"))

    # Caso extremo: Guardar libros en una ruta inválida
    def test_guardar_libros_ruta_invalida(self):
        mensaje = self.libreria.guardar_libros("/ruta/invalid/test_libreria.json")
        self.assertEqual(mensaje, "Error al guardar los libros")

    # Casos típicos
    def test_cargar_libros(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        self.libreria.guardar_libros("test_libreria.json")
        nueva_libreria = Libreria()
        mensaje = nueva_libreria.cargar_libros("test_libreria.json")
        self.assertEqual(mensaje, "Libros cargados")
        self.assertEqual(nueva_libreria.libros, [self.libro])

    # Caso extremo: Cargar libros de un archivo inexistente
    def test_cargar_libros_archivo_no_encontrado(self):
        mensaje = self.libreria.cargar_libros("archivo_no_existe.json")
        self.assertEqual(mensaje, "Archivo no encontrado")

    # Caso extremo: Cargar libros de un archivo malformado
    def test_cargar_libros_archivo_malformado(self):
        with open("test_libreria.json", "w") as f:
            f.write("contenido no válido")
        mensaje = self.libreria.cargar_libros("test_libreria.json")
        self.assertEqual(mensaje, "Error al cargar los libros")

if __name__ == '__main__':
    unittest.main()
