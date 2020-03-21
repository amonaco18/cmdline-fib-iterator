import sys

class fibiterator:
	def __init__(self, n):
		self.seq = [0,1]
		self.max = n
		self.pos = 0

	def __iter__(self):
		self.pos = 0
		self.seq = [0,1]
		return self

	def __next__(self):
		if self.pos <= self.max:
			self.pos+=1
			self.seq.append(self.seq[-1] + self.seq[-2])
			return self.seq[-1]
		else: raise StopIteration

if __name__ == "__main__":
	cmdlinearg = int(sys.argv[1]) - 1

	fib = fibiterator(cmdlinearg)
	for x in range(cmdlinearg):
		print(next(fib))
