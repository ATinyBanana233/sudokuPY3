alist=[1,2,3,4,5]

def binary_search(ilist, key):
	length=len(ilist)
	low=0
	high=length
	while (low < high):
		mid=low+(high-low)/2
		if(ilist[mid]==key):
			print mid
			return
		elif(ilist[mid] < key):
			low=mid+1
		else:
			high=mid-1
	print "fail"		
		
binary_search(alist,5)
				
