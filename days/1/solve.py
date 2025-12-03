import math
import numpy as np

def load_data(filename):
	with open(filename) as fp:
		return [line.strip() for line in fp.readlines()]

def solve(filename, part=1):
	count = 0

	data = load_data(filename)

	dial = np.array(range(0,100))
	dial = np.roll(dial, math.floor(len(dial)/2))

	print(dial)

	for instruction in data:
		delta, direction = int(instruction[1:]), -1 if instruction[:1] == "L" else 1
		for i in range(0,delta):
			dial = np.roll(dial, 1*direction)
			if part==2 and dial[0] == 0:
				count += 1

		if part==1 and dial[0] == 0:
			print("at zero", dial)
			count += 1
	
	return count

if __name__ == '__main__':
	print("Part 1 Test: ", solve('test_data.txt'))
	print("Part 1: ", solve('data.txt'))

	print("Part 2 Test: ", solve('test_data.txt', part=2))
	print("Part 2: ", solve('data.txt', part=2))
