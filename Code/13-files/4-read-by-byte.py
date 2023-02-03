import struct

with open("writeto.dat", "br") as file:
	# print(str((file.read(1).decode())))
	file.seek(0)
	print(struct.unpack("x",file.peek()))