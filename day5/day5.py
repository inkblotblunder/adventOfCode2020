#seat_data = [(row, col)] 
seat_data = []

with open ('./day5input.txt') as f:
    for line in f:
        row = line[0:7]
        col = line[7:10]
        seat_data.append((row, col))

def part1():
    max_id = 0
    uid_list = []
    for entry in seat_data:
        row = entry[0]
        col = entry[1]
        # get the row number
        row_num = binary_partition(row, 127, 'F', 'B')
        col_num = binary_partition(col, 7, 'L', 'R')

        #get unique id
        uid = (row_num * 8) + col_num
        max_id = max(uid, max_id)
        uid_list.append(uid)
    print("max_id: {}".format(max_id))
    part2(uid_list)

def part2(uid_list):
    uid_list.sort()
    taken_uid = set(uid_list)
    all_uid = set(range(uid_list[0], uid_list[-1]))
    print(all_uid)
    missing_seat = all_uid - taken_uid
    print(missing_seat)

def binary_partition(str, max_index, lo_char, hi_char):
    hi = max_index
    lo = 0
    for char in str:
        half = (hi - lo)/2
        if (char == lo_char):
            hi = lo + half
        elif (char == hi_char):
            lo = hi - half
    return hi

part1()