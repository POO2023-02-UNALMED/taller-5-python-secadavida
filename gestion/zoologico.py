from gestion.zona import Zona

class Zoologico:
	_zonas = []

	def __init__(self, nombre, ubicacion):
		self._nombre = nombre
		self._ubicacion = ubicacion

	def agregarZonas(self, zona):
		self._zonas.append(zona)

	def cantidadTotalAnimales(self):
		totalAnimales = 0

		for zona in self._zonas:
			totalAnimales += zona.cantidadTotalAnimales()

		return totalAnimales

	def getNombre(self):
		return self._nombre

	def setNombre(self, nombre):
		self._nombre = nombre
	
	def getUbicacion(self):
		return self._ubicacion

	def setUbicacion(self, ubicacion):
		self._ubicacion = ubicacion

	@classmethod
	def getZonas(cls):
		return cls._zonas

	@classmethod
	def setZonas(cls, zonas):
		cls._zonas = zonas
