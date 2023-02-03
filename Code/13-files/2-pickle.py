import pickle

# favourite_color = ["red", "green", "blue", "orange"]

# pickle.dump(favourite_color, open("save.p", "wb"))

favourite_color = pickle.load(open("save.p", "rb"))
print(favourite_color)