

def binary_search(sorted_list, target):
	low = 0
	high = len(sorted_list)-1
	
	while low <= high:
		mid = (low+high)//2
		guess = sorted_list[mid]
		if guess == target:
			return mid
		elif guess > target:
			high = mid-1
		else:
			low = mid+1
	return None

result = binary_search([1,2,3,4,5,6,7], 4)
print(result)
