arr = [2,0,6,12,1,3]
# arr = [0, 3, 6]
print(arr[len(arr):0:-1].index(arr[-1]))
print(arr[len(arr):0:-1])
th_number = 30000000
def parts(arr, th_number):
	turn_num = 0
	d = {}
	for idx, j in enumerate(arr[:-1]):
		d[j] = idx+1
	# print(d)
	for i in range(th_number-len(arr)):
		last_spoken = arr[-1]
		# print(last_spoken)
		if(last_spoken in d.keys()):
			# print(len(arr), d)
			arr.append(len(arr) - d[last_spoken])
		else:
			arr.append(0)
		d[last_spoken] = len(arr)-1
	print(arr[-1])

parts(arr, 2020)
parts(arr, 30000000)