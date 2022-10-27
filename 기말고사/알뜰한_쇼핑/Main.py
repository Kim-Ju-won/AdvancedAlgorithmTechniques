# 함수 
def if_buy(DP, check_min,n):
	check = False
	for i in range(len(DP)-1,n-1,-1):
		if check_min[1] == DP[i][1]:
			check= True
	return check

def minimum_price(k,n,product_price):
	preprocess = [[0 for _ in range(n)] for _ in range(k)]
	for i in range(k):
		for j in range(n):
			preprocess[i][j] = (product_price[i][j], j)
		preprocess[i].sort()
		
	DP = [[0,0] for _ in range(k)]
	
	# k-1번째 부터 체크
	for i in range(k-1,-1,-1):
		if i ==k-1 : 
			check_min = preprocess[i][0]
		else : 
			j = 0
			check_min = preprocess[i][j]
			# 중복으로 사면 다시 사기
			while if_buy(DP, check_min, i) :
				j+=1
				check_min = preprocess[i][j]
		DP[i] = check_min
	
	ans = 0 
	for i in range(k) : 
		ans+=DP[i][0]

	return ans


# 입력
k, n = tuple(map(int, input().split()))
product_price = [ list(map(int, input().split())) for _ in range(k)]

# 출력 
print(minimum_price(k,n,product_price))