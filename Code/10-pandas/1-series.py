import pandas as pd

s = pd.Series([3.12, 19.2, 2.8, 343])

print(s)
print(s[0])
print(s.shape)

s = pd.Series([3.12, 19.2, 2.8, 343], index=["Bradley", "Aaron", "Abby", "James"])
print(s)
print(s["James"])

s = pd.Series({
	"Bradley": 10,
	"Aaron": 12,
	"Abby": 100,
	"James": 76
})
print(s)
print(s["James"])
print(s[0])