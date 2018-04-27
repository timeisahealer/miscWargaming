cipher = "}LRMISETLVC$NAWUGFBOODARHYOCEMSJD{MGE"
print(len(cipher))
print(cipher[17])
for i in range(1, len(cipher)):
	text = ""
	for j in range(0, len(cipher)):
		text += cipher[(17+(j*i))%len(cipher)]
	print(text)




}LRMISETLVC$NAWUGFBOODARHYOCEMSJD{MGE