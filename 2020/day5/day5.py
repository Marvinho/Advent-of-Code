with open("day5_input.txt") as f:
	seats = [line.rstrip() for line in f]

print(seats)
seat_ids = []
def binaryBoarding(seats):
	
	for seat in seats:
		lower = 0
		upper = 128
		lower_col = 0
		upper_col = 8
		#print(seat)
		for char in seat[:7]:
			#print(char)
			if(char == "F"):
				upper = lower+ ((upper-lower) / 2)
			if(char == "B"):
				lower = lower + (upper-lower)/2
			#print(lower, upper)
		for char in seat[7:]:


			if(char == "R"):
				lower_col = lower_col+ ((upper_col-lower_col) / 2)
			if(char == "L"):
				upper_col = lower_col+ ((upper_col-lower_col) / 2)
			#print(lower_col, upper_col)

		seat_ids.append(lower * 8 + lower_col)
	return seat_ids
seat_ids = binaryBoarding(seats)
def yourSeatId(seat_ids):
	print(sorted(seat_ids))
	print(sum(seat_ids)-sum(range(54,879)))
	print(sum(seat_ids))
yourSeatId(seat_ids)


