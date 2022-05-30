def printChar(a, L):

	o = {}
	for i in range(L):
		
		if(a[i] in o):
			o[a[i]] = o[a[i]] + 1
		
		else:
			o[a[i]] = 1

	size = len(o)

	while (size > 0):

		cMax = 0
		amax = 0
		for key, value in o.items():

			if (value > cMax or (value == cMax and key > amax)):
				amax = key
				cMax = value

		print(f"{amax} - {cMax}")

		o.pop(amax)
		size -= 1


Str = "Mississippi"
L = len(Str)


printChar(list(Str), L)

