import math

def load_data(filename):
	with open(filename) as fp:
		return [list(map(int, line.strip().split('-'))) for line in fp.readline().split(',')]

def is_invalid(id, part):
	if part == 1:
		start = end = len(str(id))//2
		limit = 2
	else:
		start = 1
		end = len(str(id))//2
		limit = len(str(id)) 

	for i in range(start, end+1):
		pattern = str(id)[:i]
		if len(str(id).replace(pattern, '', limit)) == 0:
			return True
	
def solve(filename, expected_result, part = 1):
	data = load_data(filename)

	score = 0
	for r_min, r_max in data:
		for i in range(r_min, r_max+1):
			if is_invalid(i, part):
				score += i

	if score != expected_result:
		raise Exception(f'fuck you broke part {part} {filename} expected {expected_result} got {score}')

	return score 

if __name__ == '__main__':
	print("Part 1 Test: ", solve('test_data.txt', 1227775554))
	print("Part 1: ", solve('data.txt', 19574776074))

	print("Part 2 Test: ", solve('test_data.txt', 4174379265, part=2))
	print("Part 2: ", solve('data.txt', 25912654282, part=2))
