dist_float = 2
purpose_float = 3
days = 1
while dist_float < purpose_float:
    dist_float *= 1.1
    days += 1
print(f'Need days: {days}')