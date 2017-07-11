def multiplication_table(row,col):

	resl = [[] for i in range(row)]
	index = 0

	for r in range(1,row+1):

		for c in range(1,col+1):
			resl[index].append(r*c)
		index+=1

	return resl
