import unittest
import os
from libreria import Libreria

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

    
    def test_anadir_libro(self):
        
        #
        mensaje = self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        self.assertEqual(mensaje, "Libro añadido")
        self.assertIn(self.libro, self.libreria.libros)
    

    def test_buscar_libro(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        resultado = self.libreria.buscar_libro('Cien años de soledad')
        self.assertEqual(resultado, [self.libro])
    
    
    def test_buscar_por_autor(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        resultado = self.libreria.buscar_por_autor('Gabriel García Márquez')
        self.assertEqual(resultado, [self.libro])
    

    def test_eliminar_libro(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        mensaje = self.libreria.eliminar_libro('Cien años de soledad')
        self.assertEqual(mensaje, "Libro no eliminado")
        self.assertNotIn(self.libro, self.libreria.libros)
    

    def test_guardar_libros(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        mensaje = self.libreria.guardar_libros("test_libreria.json")
        self.assertEqual(mensaje, "Libros guardados")
        self.assertTrue(os.path.exists("test_libreria.json"))
    

    def test_cargar_libros(self):
        self.libreria.anadir_libro(self.libro['titulo'], self.libro['autor'], self.libro['genero'], self.libro['anio'])
        self.libreria.guardar_libros("test_libreria.json")
        nueva_libreria = Libreria()
        mensaje = nueva_libreria.cargar_libros("test_libreria.json")
        self.assertEqual(mensaje, "Libros cargados")
        self.assertEqual(nueva_libreria.libros, [self.libro])
    

    def test_cargar_libros_archivo_no_encontrado(self):
        '''Prueba el manejo del error en el método cargar_libros cuando el archivo no existe.'''
        mensaje = self.libreria.cargar_libros("archivo_no_existe.json")
        self.assertEqual(mensaje, "Archivo no encontrado")

if __name__ == '__main__':
    unittest.main()
