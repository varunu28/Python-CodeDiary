def check_OutOfBound(arr,n):
	try:
		temp = arr[n]
	except:
		temp = "Don't try buffer overflow attacks in Python"
	return temp

arr = [1,2,3,4]
print(check_OutOfBound(arr,3)) # Returns 4
print(check_OutOfBound(arr,4)) # Returns error warning