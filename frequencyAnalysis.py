import operator

string = "HUNNBTV ENTWUC T JDLU DV FTFFTIU KDCTW, TK NUTAK, O KHOVL OK QTA T JDLU, OK HTA ADBUKHOVI KD CD QOKH AKXUUK BMAOY. FTFFTIU FUYTBU EXUKKW BTC. TVWQTWA, BW YDBEMKUX OA EUXGDXBOVI RMOKU QUNN, KHU GTYK OK OA UNUYKXOYTN EXDPOCUA TV COAKOVYK TCPTVKTIU DPUX KHU TVTNWKOYTN UVIOVU. ADDV O HDEU FTFFTIU AUUA XUTADV TVC MECTKUA HOA CUAOIVA"

order_freq = "ETAOINSRHDLUCMFYWGPBVKXQJZ"
def freqAnalysis(string):
	freq = {}
	for char in string:
		if (char.isalpha() == False):
			continue
		if char not in freq:
			freq[char] = 1
		else:
			count = freq[char]
			freq[char] = count + 1
	sorted_items = sorted(freq.items(), key = operator.itemgetter(1))
	sorted_items.reverse()
	mapping = {}
	for i in range(len(sorted_items)):
		item = sorted_items[i]
		mapping[item[0]] = order_freq[i]
		print(sorted_items[i][0], order_freq[i])

	temp = mapping['T']
	mapping['T'] = 'A'
	mapping['K'] = temp
	
	for char in string:
		if char.isalpha():
			print(mapping[char], end="")
		else:
			print(char, end="")


freqAnalysis(string)
