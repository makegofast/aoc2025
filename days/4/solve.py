import sys
import itertools

def load_data(filename):
	with open(filename) as fp:
		return [list(line.strip()) for line in fp.readlines()]

def find_rolls(map):
	locations = []

	for row, line in enumerate(map):
		for col, char in enumerate(line):
			if char=='@':
				locations.append([row, col])
	
	return locations

def scan_around(c_row, c_col, map):
	directions = [
		[0, -1],
		[0, 1],
		[-1, 0],
		[1, 0],
		[-1, -1],
		[-1, 1],
		[1, -1],
		[1, 1]
	] 

	rolls_around = 0

	for (s_row, s_col) in directions:
		t_row, t_col = c_row+s_row, c_col+s_col

		if t_row < 0 or t_col < 0:
			continue

		try:
			char_at = map[c_row + s_row][c_col + s_col]
		except IndexError:
			char_at = ''

		if char_at == "@":
			rolls_around += 1

		#print(f'({c_row},{c_col} + {s_row},{s_col} -> {c_row+s_row},{c_col+s_col} = {char_at} (count={rolls_around})')

	return rolls_around

def remove_rolls(map, targets):
	for (row, col) in targets:
		map[row][col] = 'x'
	
	return len(targets)

def print_map(map):
	for row, line in enumerate(map):
		print(''.join(line))

def solve(filename, expected, part=1):
	map = load_data(filename)
	
	total_removed = 0

	while True:
		accessible_locations = []

		locations = find_rolls(map)
		for (row, col) in locations:
			rolls_around = scan_around(row, col, map)
			if rolls_around < 4:
				accessible_locations.append([row, col])
		
		rolls_removed = remove_rolls(map, accessible_locations)
		total_removed += rolls_removed

		#print_map(map)

		if part==1 or (part==2 and rolls_removed==0):
			break

	result = total_removed 

	if not expected or result != expected:
		print(f'❌ fuck you broke part {part} {filename}: expected {expected} got {result})')
		sys.exit()
	else:
		print(f'✅ part {part} {filename} = {result}')

if __name__ == '__main__':
	solve('test_data.txt', 13)
	solve('data.txt', 1397)

	solve('test_data.txt', 43, part=2)
	solve('data.txt', 8758, part=2)
