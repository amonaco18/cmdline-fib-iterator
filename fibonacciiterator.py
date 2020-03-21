import sys

class fibiterator:
	def __init__(self, n):
		self.n = [0,1]
		self.max = n
		self.seq = 0

	def __iter__(self):
		self.seq = 0
		self.n = [0,1]
		return self

	def __next__(self):
		if self.seq <= self.max:
			self.seq+=1
			self.n.append(self.n[-1] + self.n[-2])
			return self.n[-1]
		else: raise StopIteration

if __name__ == "__main__":
	cmdlinearg = int(sys.argv[1]) - 1

	fib = fibiterator(cmdlinearg)
	for x in range(cmdlinearg):
		print(next(fib))
