'''
from itertools import combinations

A=[1,2,3,4]
for i in range(1,3):
	print(list(combinations(A,i)))
#print (list(combinations(A,4))

'''
from itertools import combinations

#token=input().split()
token="HACK 3"
token=token.split()
str1= str(token[0])
size=int(token[1])
fl=[]
for i in range(1,size+1):
	#fl.append(list(combinations(str1,i)))
	fl.append(list(combinations(str1,i)))
word=""
flw=[]
list1=[]
print (len(fl))
#print (fl)
flat_list = []
for sublist in fl:
	print (sublist)


	for i in range(len(sublist)):
		word=""
		for c in sublist[i]:
		        word=word+c
		flw.append(word)
		flw.sort()
		print(flw)
for i in flw:
        print (i)


'''
	for item in sublist:
		print(list(item))
		print("+++++++")


for i in range(len(sublist)):
    word=""
    for c in sublist[i]:
        word=word+c
    flw.append(word)
flw.sort()
for i in flw:
        print (i)

'''


