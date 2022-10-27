import sys
INT_MAX = sys.maxsize
# 함수 
def make_team(n,array):
	array.sort()
	check_min = INT_MAX 
	for i in range(n):
		temp = array[i]+array[-i-1]
		check_min = min(check_min, temp)
		
	return check_min
	
# 입력
n = int(input())
array  = list(map(int, input().split()))
print(make_team(n,array))