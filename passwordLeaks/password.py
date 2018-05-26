# from sets import Set

f = open("passwordLeaks.txt", "r")
lines = f.readlines()
lines = [line.rstrip('\n') for line in lines]

# hmap = {}
# predecessors = {}
# start = "abcdefghijklmnopqrstuvwxyz"
# for char in start:
# 	hmap[char] = 0
# 	hmap[char.upper()] = 0
# 	predecessors[char] = Set()

dictionary = {}

for line in lines:
	char = line[1]
	if line[1] not in dictionary:
		dictionary[line[1]] = set()
	if line[2] not in dictionary:
		dictionary[line[2]] = set()
	assert(dictionary[line[1]] != None)
	assert(dictionary[line[2]] != None)
	# print(type(dictionary[line[2]]))
	dictionary[line[1]].add(line[0])
	dictionary[line[2]].add(line[0])
	dictionary[line[2]].add(line[1])

orderedList = {}
for entry in dictionary:
	# print(entry + ": " + str(dictionary[entry]))
	l = len(dictionary[entry])
	if (l not in orderedList):
		orderedList[l] = []
	orderedList[l] = orderedList[l] + [entry]

print(str(orderedList))
# ans = '{' + ans
# print(ans[::-1])



