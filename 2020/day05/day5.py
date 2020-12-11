with open("day5_input.txt") as f:
	seats = [line.rstrip() for line in f]

#print(seats)
seat_ids = []
def binaryBoarding(seats):
	
	for seat in seats:
		seat_id = int(seat.replace("F","0").replace("B","1").replace("L","0").replace("R","1"),2)

		seat_ids.append(seat_id)
	return seat_ids

seat_ids = binaryBoarding(seats)
print(max(seat_ids))

def yourSeatId(seat_ids):
	#print(sorted(seat_ids))
	print(sum(range(min(seat_ids),max(seat_ids)+1))-sum(seat_ids))
	#print(sum(seat_ids))

yourSeatId(seat_ids)


