dialcodes = {"us": "+1", "nl": "+31", "no": "+47", "it": "+39"}

print(dialcodes.setdefault("it", "???")) # +39 
print(dialcodes.pop("it"))  # +39
print(dialcodes.setdefault("it", "???")) # "???"
print(dialcodes.pop("it"))  # ???
