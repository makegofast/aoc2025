import sys
import itertools
import math

def load_data(filename):
	data = []

	with open(filename) as fp:
		return [l.strip('\n') for l in fp.readlines()]
	
def calc_distance(a, b):
	a = list(map(int, a.split(',')))
	b = list(map(int, b.split(',')))

	return math.dist(a, b)

def add_circuit(pair, circuits):
	a, b = pair
	related = set() 
	unrelated = []

	for i, circuit in enumerate(circuits):
		if a in circuit or b in circuit:
			#print(f'{circuit} contains {a} or {b}, marking related')
			related.update(circuit)
			related.add(a)
			related.add(b)
			#print(f' related now {related}')
		else:
			#print(f'{circuit} is unrelated')
			unrelated.append(circuit)
	
	#print(f'unrelated {unrelated}')
	#print(f'related   {related}')

	if not related:
		#print(f'adding {a} - {b}')
		unrelated.append(set([a, b]))
	else:
		unrelated.append(related)

	#print(f'result {unrelated}')

	return unrelated

def solve(filename, expected, part=1):
	data = load_data(filename)

	pairs = set(itertools.combinations(data, r=2))
	pairs = sorted(pairs, key=lambda x: calc_distance(x[0], x[1]))

	length = 10 if 'test' in filename else 1000

	#for pair in pairs:
	#	print(pair, calc_distance(pair[0], pair[1]))
	
	circuits = [] 
	last_count = None
	for i in range(0, length if part == 1 else len(pairs)):
		circuits = add_circuit(pairs[i], circuits)
		if part == 2:
			print(circuits)
			print(f'pair: {i}, circuits: {len(circuits)} {pairs[i]}')
		if part == 2 and len(circuits[0]) == len(data): 
			last_pair = pairs[i]
			break
		
		last_count = len(circuits)

	if part == 1:
		circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
		result = math.prod([len(c) for c in circuits[0:3]])
	else:
		print(f'last pair {last_pair}')
		result = math.prod([int(p.split(',')[0]) for p in last_pair])

	if not expected or result != expected:
		print(f'❌ fuck, you broke part {part} {filename}: expected {expected} got {result})')
		sys.exit()
	else:
		print(f'✅ part {part} {filename} = {result}')

if __name__ == '__main__':
	solve('test_data.txt', expected=40)
	solve('data.txt', expected=131150)

	solve('test_data.txt', expected=25272, part=2)
	solve('data.txt', 2497445, part=2)
