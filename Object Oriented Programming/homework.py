import math

class Line():
	def __init__(self, coor1, coor2):
		self.coor1 = coor1
		self.coor2 = coor2

	def distance(self):
		return math.sqrt((self.coor2[1] - self.coor1[1])**2 + (self.coor2[0] - self.coor1[0])**2)

	def slope(self):
		return (self.coor2[1] - self.coor1[1]) / (self.coor2[0] - self.coor1[0])

	def __str__(self):
		return f"({self.coor1}-{self.coor2})"

class Cylinder:
	def __init__(self, height=1, radius=1):
		self.height = height
		self.radius = radius

	def volume(self):
		return math.pi * (self.radius**2) * self.height

	def surface_area(self):
		return 2*math.pi*self.radius * self.height + 2 * math.pi * (self.radius**2)

	def __str__(self):
		return f"(h={self.height}, r={self.radius})"

def main():
	line = Line((3, 2), (8, 10))
	print("Line", line)
	print("Distance:", line.distance())
	print("Slope:", line.slope())
	print("")

	cylinder = Cylinder(2, 3)
	print("Cylinder", cylinder)
	print("Volume:", cylinder.volume())
	print("Surf. area:", cylinder.surface_area())


if __name__ == "__main__":
	main()
