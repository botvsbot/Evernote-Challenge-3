
N = raw_input()
N = int(N)

list = []
pdct = 1
zero_cnt = 0
j = 0
while(N > 0):
	try:
		i = int(raw_input())
	except ValueError:
		print "Invalid input, Quitting."
		pdct = 0
		break
	list.append(i)
	if i == 0:
		if zero_cnt == 0:
			index = j
		zero_cnt += 1
		N -= 1
		j += 1
		continue
	pdct *= i
	N -= 1
	j += 1
		
product_list = []

if zero_cnt == 1:
	product_list = [0 for i in list]
	product_list[index] = pdct
elif zero_cnt > 1:
	product_list = [0 for i in list]
else:
	for i in xrange(0,len(list)):
		product_list.append(pdct/list[i])

for item in product_list:
	print item
