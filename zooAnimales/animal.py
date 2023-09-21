import zooAnimales

class Animal:
	_totalAnimales = 0

	def __init__(self, nombre, edad, habitat, genero, zona = None):
		self._nombre = nombre
		self._edad = edad
		self._habitat = habitat
		self._genero = genero
		self._zona = zona
		Animal._totalAnimales += 1

	@classmethod
	def getTotalAnimales(cls):
		return cls._totalAnimales

	@classmethod
	def setTotalAnimales(cls, totalAnimales):
		cls._totalAnimales = totalAnimales

	def movimiento(self):
		return "desplazarse"

	@staticmethod
	def totalPorTipo():
		return "Mamiferos : " + str(zooAnimales.mamifero.Mamifero.cantidadMamiferos()) + "\n" + \
		"Aves : " + str(zooAnimales.ave.Ave.cantidadAves()) + "\n" + \
		"Reptiles : " + str(zooAnimales.reptil.Reptil.cantidadReptiles()) + "\n" + \
		"Peces : " + str(zooAnimales.pez.Pez.cantidadPeces()) + "\n" + \
		"Anfibios : " + str(zooAnimales.anfibio.Anfibio.cantidadAnfibios())

	def toString(self) -> str:
		string = "Mi nombre es " + str(self._nombre) + ", tengo una edad de " + str(self._edad) + \
		", habito en " + str(self._habitat) + " y mi genero es " + str(self._genero)

		if (self._zona != None):
			string += ", la zona en la que me ubico es " + str(self._zona) + ", en el " + str(self._zona.getZoo())

		return string

	def getNombre(self): 
		return self._nombre
	

	def setNombre(self, nombre): 
		self._nombre = nombre
	

	def getEdad(self): 
		return self._edad
	

	def setEdad(self, edad): 
		self._edad = edad
	

	def getHabitat(self): 
		return self._habitat
	

	def setHabitat(self, habitat): 
		self._habitat = habitat
	

	def getGenero(self): 
		return self._genero
	

	def setGenero(self, genero): 
		self._genero = genero
	

	def getZona(self): 
		return self._zona
	

	def setZona(self, zona): 
		self._zona = zona
	

