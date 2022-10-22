print("Enter value (USD) here:")
usd = input()
vnd = int(usd) * 23000 # "usd" must be an integer or the result would be 1 in 23 times (11111...111)
print(str(usd) + " USD = " + str(vnd) + "VND")