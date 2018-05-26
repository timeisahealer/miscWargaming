# PRUH FLSKHUWHAW WRGDB, ORRNV WR EH HQFUBSWHG WKH VDPH ZDB DV BHVWHUGDBV - ZLOO XSGDWH VRRQ, 3

#"QPQQPWU'I UEWYEU QUNNUK XGKKL GR HYNX DL 10 BSOBSC SBYESYTUESU YETUJ, Y XPFUE'N WBN POO TPL" | tr '[PQSTUVWXYZCODEBRAKINGFHJLM]' '[A-Z]'

def decipher(ciphertext, shift):
	for P in ciphertext:
		if P.isalpha():
			if (ord(P) - shift < ord('A')):
				print(chr(ord(P) - shift + 26), end="")
			else:
				print(chr(ord(P) - shift), end="")
		else:
			print(P, end="")
	print()



ciphertext = input()
shift = 3

for i in range(26):
	decipher(ciphertext, i)