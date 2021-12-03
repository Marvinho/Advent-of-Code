import numpy as np

with open("day03.txt") as f:
	diagnostics = [line.rstrip() for line in f]
# print(np.array(diagnostics))
def count_pos(diagnostics):
	count = {}
	for i in range(len(diagnostics[0])):
		count[i] = 0

	for diagnostic in diagnostics:
		for i, c in enumerate(diagnostic):
			if(c == '1'):
				count[i] += 1
	return count

def calc_power_consumption(diagnostics, count):
	gamma_str = ""
	epsilon_str = ""
	for key, value in count.items():
		print(key, value)
		if(value > len(diagnostics)/2):
			gamma_str+="1"
			epsilon_str+="0"
	
		else:
			gamma_str+="0"
			epsilon_str+="1"
		gamma_int = int(gamma_str, 2)
		epsilon_int = int(epsilon_str, 2)
	power_consumption = gamma_int*epsilon_int			
	print("power_consumption: {}".format(power_consumption))
	return power_consumption, gamma_str, epsilon_str

count = count_pos(diagnostics)
power_consumption, gamma_str, epsilon_str = calc_power_consumption(diagnostics, count)

def calc_life_support_rating(diagnostics):
	oxys = diagnostics
	oxy_result = diagnostics
	i = 0
	while(len(oxy_result) != 1):
		oxy_dict = count_pos(oxy_result)
		number_of_oxys = len(oxy_result)
		oxys = oxy_result
		oxy_result = []

		if(oxy_dict[i] >= number_of_oxys/2):
			for j, oxy in enumerate(oxys):
				if(oxy[i] == "1"):
					oxy_result.append(oxys[j])
		else:
			for j, oxy in enumerate(oxys):
				if(oxy[i] == "0"):
					oxy_result.append(oxys[j])
		i+=1
	print(oxy_result)
	oxy_gen_rating = oxy_result[0]

	oxys = diagnostics
	oxy_result = diagnostics
	i = 0
	while(len(oxy_result) != 1):
		oxy_dict = count_pos(oxy_result)
		number_of_oxys = len(oxy_result)
		oxys = oxy_result
		oxy_result = []

		if(oxy_dict[i] >= number_of_oxys/2):
			for j, oxy in enumerate(oxys):
				if(oxy[i] == "0"):
					oxy_result.append(oxys[j])
		else:
			for j, oxy in enumerate(oxys):
				if(oxy[i] == "1"):
					oxy_result.append(oxys[j])
		i+=1
	print(oxy_result)
	co2_gen_rating = oxy_result[0]

	life_support_rating = (int(oxy_gen_rating, 2))*(int(co2_gen_rating, 2))
	print(life_support_rating)
	return life_support_rating
life_support_rating = calc_life_support_rating(diagnostics)




