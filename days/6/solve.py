import sys
import operator 
import itertools
import functools

def load_data(filename):
	with open(filename) as fp:
		data = [line.strip('\n') for line in fp.readlines()]
		ops = data.pop()
		max_width = max([len(l) for l in data])
		right = max_width
		for left in reversed([i for i, v in enumerate(ops) if v != ' ']):
			values = []
			for line in data:
				values.append(line[left:right]) 

			yield(ops[left], values)
			right = left-1

def cephalize(values):
	i = 0
	while i<len(values[0]):
		yield ''.join([v[i] for v in values]).strip()
		i += 1
	
def solve(filename, expected, part=1):
	data = load_data(filename)

	func_map = {'+': operator.add, '*': operator.mul}

	grand_total = 0

	for oper, values in load_data(filename):
		if part==2:
			values = cephalize(values)

		total = functools.reduce(func_map[oper], map(int, values)) 
		grand_total += total

	result = grand_total 

	if not expected or result != expected:
		print(f'❌ fuck you broke part {part} {filename}: expected {expected} got {result})')
		sys.exit()
	else:
		print(f'✅ part {part} {filename} = {result}')

if __name__ == '__main__':
	solve('test_data.txt', 4277556)
	solve('data.txt', 3525371263915)

	solve('test_data.txt', 3263827, part=2)
	solve('data.txt', None, part=2)
