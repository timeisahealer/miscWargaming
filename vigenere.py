ciphertext = "AM W VFTTYOSASW YPV EPGBBM TN ZRIGYATYQFR LF OWL MMRH LL DCNQL SI QWNOMNDV, IYWU HATCXL DUJCKIQEK WG TM YTZDYOS UCM UWJWLTSS"
key = "SHOTFIRED"
i = 0
for char in ciphertext:
	if char.isalpha() == False:
		print(char, end="")
		continue
	asc = ord(char) - ord(key[i%len(key)]) + ord('A')
	if asc < ord('A'):
		asc += 26
	i += 1
	print(chr(asc), end="")