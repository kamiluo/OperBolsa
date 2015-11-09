
from appBolsa.logic.LibroOrdenes import LibroOrdenes
from  appBolsa.logic.Pool import PoolConexiones
class Principal():
    def __init__(self):
        self.pathAchivoAcciones = ""
        self.libroOrdenes = LibroOrdenes()
        self.poolConexiones = PoolConexiones()
    def cargarPool(self):
        self.poolConexiones.start()
    def cargarLibroOrdenes(self):
        """
        Carga el archivo de xml con la informacion base del libro de ordenes
        """
        self.libroOrdenes.cargar(self.pathAchivoAcciones)

