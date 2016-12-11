class jugador():
	def __init__(self,nombre,apellidos,nickname=""):
		self.nombre=nombre
		self.apellidos=apellidos
		self.nickname=nickname
		jugador.cantidad+=1
		
	cantidad=0
	
	def setNombre(self,nombre):
		self.nombre=nombre
		print("El nombre del jugador ha sido cambiado a "+nombre)
			
	def getNombre(self):
			return self.nombre
			
	def setApellidos(self,apellidos):
			self.apellidos=apellidos
			print("El nombre del jugador ha sido cambiado a "+apellidos)
			
	def getApellidos(self):
			return self.apellidos
			
	def setNickname(self,nickname):
			self.nickname=nickname
			print("El nombre del jugador ha sido cambiado a "+nickname)
			
	def getNickname(self):
			return self.nickname
			
Mario=jugador("Mario","Durantez Stolle","Warb")
print Mario.nombre
print Mario.getNombre()
print Mario.getApellidos()
print Mario.getNickname()

print jugador.cantidad

class LIGA_MAGIC():
	def __init__(self,jugadores,coleccion,formato="",fecha_comienzo)
	
	def setJugadores(self,jugadores):
		self.jugadores=jugadores
		print("Los participantes de esta liga son: "+jugadores)
			
	def getJugadores(self):
			return self.jugadores
			
	def setColeccion(self,coleccion):
		self.coleccion=coleccion
		print("La coleccion empleada para jugar esta liga es "+coleccion)
			
	def getColeccion(self):
			return self.coleccion
			
	def setFormato(self,formato):
		self.formato=formato
		print("El formato de esta liga es "+formato)
			
	def getFormato(self):
			return self.formato
			
	def setFecha_comienzo(self,fecha_comienzo):
		self.fecha_comienzo=fecha_comienzo
		print("Esta liga oficialmente tuvo comienzo el "+fecha_comienzo)
			
	def getFecha_comienzo(self):
			return self.fecha_comienzo