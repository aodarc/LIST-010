import math

class HumanTextManager:
	def __init__(self, file):
		self.file = file
		self.paragraph = 0

	def __enter__(self):
		self.paragraph += 1
		return self

	def __exit__(self, *args):
		self.paragraph -= 1

	def write(self, text: str):
		return self.file.write('\t'*self.paragraph + text + '\n')


print('HUMAN CODE')

if __name__ == '__main__':
	stdout = open('./stdout.txt', 'w+')

	writer = HumanTextManager(file=stdout)

	writer.write('Some Text')
	writer.write('Some Text')
	with writer:
		writer.write('Some Text')
		with writer:
			writer.write('Some Text')
	writer.write('Some Text')

