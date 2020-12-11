with open("test.txt") as f:
	a = f.read()
	a = a.strip()
	b = a.split("\n\n")
	print(b)
	#lines = [line.rstrip() for line in f]
b = [x.replace("\n"," ") for x in b]
#print(a)
print(b)
#print(lines)
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
num_valid_passports = 0
def passportProcessing(b, fields, num_valid_passports):
	for i in b:
		passport_dict = {}
		#print(i)
		i = i.split(" ")
		for j in i:

			j = j.split(":")
			#print(j)
			passport_dict[j[0]] = j[1]
		#print(asdf)
		if(all(field in passport_dict for field in fields)):
			if(dataValidation(passport_dict)):
				num_valid_passports += 1

	return num_valid_passports

def dataValidation(passport_dict):
	valid_ecls = ["amb", "blu","brn", "gry", "grn", "hzl", "oth"]
	print(passport_dict)
	if(int(passport_dict["byr"]) < 1920 or int(passport_dict["byr"]) > 2002):
		return False
	
	print(passport_dict["iyr"])
	if(int(passport_dict["iyr"]) < 2010 or int(passport_dict["iyr"]) > 2020):
		return False
	
	print(passport_dict["eyr"])
	if(int(passport_dict["eyr"]) < 2020 or int(passport_dict["eyr"]) > 2030):
		return False

	print(passport_dict["hgt"])
	if(passport_dict["hgt"][-2:] =="cm"):
		if(int(passport_dict["hgt"][:-2]) < 150 or int(passport_dict["hgt"][:-2]) > 193):
			return False
	elif(passport_dict["hgt"][-2:] =="in"):
		if(int(passport_dict["hgt"][:-2]) < 59 or int(passport_dict["hgt"][:-2]) > 76):
			return False
	else:
		return False

	print(passport_dict["hcl"])
	print(passport_dict["hcl"][0], passport_dict["hcl"][0] != "#", len(passport_dict["hcl"][1:]) != 6)
	if(passport_dict["hcl"][0] != "#" or len(passport_dict["hcl"][1:]) != 6):
		return False
	else:
		for i in passport_dict["hcl"][1:]:
			if((not i.isdigit()) and (i not in "abcdef")):
				return False

	print(passport_dict["ecl"])	
	if(passport_dict["ecl"] not in valid_ecls):
		return False

	print(passport_dict["pid"])
	if(len(passport_dict["pid"]) != 9 or (not passport_dict["pid"].isdigit())):
		return False

	return True

#result = passportProcessing(b, fields, num_valid_passports)
#print(result)