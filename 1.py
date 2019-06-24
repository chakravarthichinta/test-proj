#noofshoes = int(input())
noofshoes = 10
#shoesize=[]
#shoesize=list(map(int,input().split()))
shoesize=[2,3,4,5,6,8,7,6,5,18]
#cust=int(input())
cust=6
item_list=[]
'''
for i in range(6):
	item_list.append(list(map(int,input().split() )))
'''

item_list=[[6,55],[6,45],[6,55],[4,40],[15,60],[10,50]]
print(item_list)
print("-------------------clear")
sum1=0
for i in range(len(item_list)):
	print(item_list[i][0])
	for x in shoesize:
		
		print(x)
'''
		if(item_list[i][0]==x):
			sum1=sum1+item_list[i][1]
			print("sum is......",sum1)
			item_list.remove(item_list[i])
			shoesize.remove(x)
			break
		else:
			sum1=sum1+0
print(sum)
	
'''


'''
0
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45clear
6 55
4 40
18 60
10 50

Sample Output

200

Explanation

Customer 1: Purchased size 6 shoe for $55.
Customer 2: Purchased size 6 shoe for $45.
Customer 3: Size 6 no longer available, so no purchase.
Customer 4: Purchased size 4 shoe for $40.
Customer 5: Purchased size 18 shoe for $60.
Customer 6: Size 10 not available, so no purchase.

Total money earned =


'''
