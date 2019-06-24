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
sum1=0
for i in range(len(item_list)):

     if(item_list[i][0]==x for x in shoesize):
            print("list_item",item_list[i][1])
            sum1=sum1+item_list[i][1]
            print("sum is......",sum1)
            #item_list.remove(item_list[i])
	    print("-------------",x)
	    print(item_list)
	    print(shoesize)

	    break
     else:
            sum1=sum1+0
	    print(shoesize)
print(sum1)
    



