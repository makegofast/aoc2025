import sys

def load_data(filename):
	fresh_ranges = []
	ingredients = []

	with open(filename) as fp:
		for line in [l.strip() for l in fp.readlines()]:
			if '-' in line:
				fresh_ranges.append(list(map(int, line.split('-'))))
			elif line:
				ingredients.append(int(line))

		return fresh_ranges, ingredients

def in_range(id, ranges):
	for range in ranges:
		if range[0] <= id <= range[1]:
			return True

def merge_ranges(ranges):
	change_count = 0
	merged = []
	for r_start, r_end in sorted(ranges):
		updated = False
		for m_index, (m_start, m_end) in enumerate(merged):
			if r_start <= m_start <= r_end <= m_end:
				merged[m_index][0] = r_start
				updated = True
				break
			elif m_start <= r_start <= m_end <= r_end:
				merged[m_index][1] = r_end
				updated = True
				break
			elif r_start <= m_start <= m_end <= r_end:
				merged[m_index] = [r_start, r_end]
				updated = True
				break
			elif m_start <= r_start <= r_end <= m_end:
				updated = True
				break
			
		if updated:
			change_count += 1
		if not updated:
			merged.append([r_start, r_end])
		
	return change_count, merged 

def solve(filename, expected, part=1):
	fresh_ranges, ingredients = load_data(filename)
	result = 'foo'

	if part==1:
		fresh_ids = []
		for id in ingredients:
			if in_range(id, fresh_ranges):
				fresh_ids.append(id)
		result = len(fresh_ids)
	else:
		while True:
			update_count, fresh_ranges = merge_ranges(fresh_ranges)
			if update_count == 0:
				break

		result = 0

		for range in fresh_ranges:
			result += range[1] - range[0] + 1

	if not expected or result != expected:
		print(f'❌ fuck you broke part {part} {filename}: expected {expected} got {result})')
		sys.exit()
	else:
		print(f'✅ part {part} {filename} = {result}')

if __name__ == '__main__':
	solve('test_data.txt', 3)
	solve('data.txt', 607)

	solve('test_data.txt', 14, part=2)
	solve('data.txt', 342433357244012, part=2)
