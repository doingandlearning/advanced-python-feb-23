x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

def get_key(item):
	return item[1]

sorted_dict = dict(sorted(x.items(), key=get_key))

print(sorted_dict)