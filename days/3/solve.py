import sys

def load_data(filename):
	with open(filename) as fp:
		return [list(map(int, list(line.strip()))) for line in fp.readlines()]

def optimize_joltage(bank, batteries_required):
	batteries = []
	
	#print()
	#print(bank)
	while len(batteries) < batteries_required:
		start = batteries[-1]+1 if len(batteries) else 0 
		end = len(bank)-batteries_required+len(batteries)+1
		#print (bank, start, end, batteries, bank[start:end])
		batteries.append(bank.index(max(bank[start:end]), start))

	return int(''.join([str(bank[i]) for i in batteries]))

def solve(filename, expected, part = 1):
	total_joltage = 0
	for bank in load_data(filename):
		joltage = optimize_joltage(bank, 12 if part == 2 else 2)
		#print(bank, joltage)
		total_joltage += joltage

	if not expected or total_joltage != expected:
		print(f'❌ fuck you broke part {part} {filename}: expected {expected} got {total_joltage})')
		sys.exit()
	else:
		print(f'✅ part {part} {filename} = {total_joltage}')

if __name__ == '__main__':
	solve('test_data.txt', 357)
	solve('data.txt', 17427)

	solve('test_data.txt', 3121910778619, part=2)
	solve('data.txt', 173161749617495, part=2)
