def banner(start, end):
	return lambda msg: f"{start} {msg} {end}"

happyBanner = banner("😁","😁")
sadBanner = banner("😟","😟")

# thisBanner = banner(config.startBanner, config.endBanner)

print(happyBanner("Functional programming is cool!"))
print(sadBanner("Noone will pass it during code review - they want OOP"))