import numpy as np
with open("day11.txt") as f:
	energy_levels = []
	for line in f:
		energy_levels.append([int(x) for x in line.strip()])

energy_levels = np.asarray(energy_levels)
energy_levels = np.pad(energy_levels, pad_width=1, mode='constant', constant_values=0)
# print(energy_levels)

def flashing(energy_levels, flash_counter):
	alrdy_flashed = np.zeros((10,10), dtype=bool)
	alrdy_flashed = np.pad(alrdy_flashed, pad_width=1, mode='constant', constant_values=True)
	# print(alrdy_flashed)
	
	energy_levels = energy_levels + 1
	# print(energy_levels)
	while(True):
		b = np.where(energy_levels > 9)
		# print(b)
		remainder = np.copy(alrdy_flashed)
		for i, j in zip(b[0], b[1]):
			# print(energy_levels[i][j])
			if(alrdy_flashed[i][j] == False):
				alrdy_flashed[i][j] = True
				energy_levels[i-1][j-1] += 1
				energy_levels[i-1][j] += 1
				energy_levels[i-1][j+1] += 1
				energy_levels[i][j-1] += 1
				energy_levels[i][j+1] += 1
				energy_levels[i+1][j-1] += 1
				energy_levels[i+1][j] += 1
				energy_levels[i+1][j+1] += 1
		# print(remainder)
		# print(np.array_equal(remainder, alrdy_flashed))
		if(np.array_equal(remainder, alrdy_flashed)):
			break
	flash_counter += (energy_levels > 9).sum()
	b = np.where(alrdy_flashed == True)
	for i, j in zip(b[0], b[1]):
		energy_levels[i][j] = 0
	# print(energy_levels)
	return energy_levels, flash_counter

if __name__=="__main__":
	flash_counter = 0
	for i in range(1, 101):
		energy_levels, flash_counter = flashing(energy_levels, flash_counter)
		if(i%10 == 0):
			print("After step ", i, energy_levels)
			print(flash_counter)