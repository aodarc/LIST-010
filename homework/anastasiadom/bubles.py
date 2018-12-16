import math

class Bubble:
	def __init__(self, name, radius=0, enableRadius=True):
		self.name = name
		self.radius = 0
		if isinstance(radius,int):
			self.radius = radius
		self.enableRadius = enableRadius
		

	def setRadius(self, radius):
		if self.enableRadius == True:
			self.radius = radius
		else:
			print("Don't change my radius")

	def getRadius(self):
		return self.radius

	@property
	def volume(self):
		return (4/3*math.pi*(self.radius)**3)
	
	@property
	def square(self):
		return (4*math.pi*(self.radius)**2)

	def addBubble(self, item):

		volume = 0
		if isinstance(item, Bubble):
			volume = item.volume

		sumVolume = self.volume + volume
		self.radius = (3 * sumVolume / (4 * math.pi))**(1/3)

	def removeBubble(self, item):

		volume = 0
		if isinstance(item, Bubble):
			volume = item.volume

		removeVolume = self.volume - volume
		self.radius = (3 * removeVolume / (4 * math.pi))**(1/3)

bubbleGubble = Bubble('Gubble',32)
bubbleTruble = Bubble('Truble',10, False)

print(bubbleGubble.volume)

bubbleGubble.addBubble(bubbleTruble)

print(bubbleGubble.volume)

bubbleGubble.removeBubble(bubbleTruble)

print(bubbleGubble.volume)