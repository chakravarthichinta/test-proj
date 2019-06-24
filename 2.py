char= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','t','u','v','w','x','y','z']
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26]
#range1=int(input())
range1=3
result = "-".join(char[range1-1::-1]+char[1:range1:])
print(result)
print(len(result))
print(type(result))


for i in range(range1+1,2):
	print(result[i])


"""

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

"""
