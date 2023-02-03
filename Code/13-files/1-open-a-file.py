import json
# house = open("213AnywhereAve.txt")

# try:
# 	print(house.read())
# finally:
# 	house.close()



# with open("213AnywhereAve.txt", "r") as house:
# 	with open("otherhouse.txt", "w") as new_house:
# 		for i in range(10):
# 			house.seek(i)
# 			new_house.write(house.readline())
# 		for i in range(10):
# 			house.seek(10-i)
# 			new_house.write(house.readline())

with open("data.json", "w+") as file:
	data = json.loads(file.read())
	print(data)
	with open("tattooine.txt", "w") as tat:
		tat.write(f'{data["name"]} has a rotation period of {data["rotation_period"]}')
		data['name'] = "NotTat!"
		file.write(json.dumps(data))