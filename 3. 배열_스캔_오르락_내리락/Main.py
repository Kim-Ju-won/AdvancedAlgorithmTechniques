'''
알고리즘 설명 : 
이 알고리즘은 배열을 순서대로 스캔하여 "오르락 내리락 규칙을 확인하고" 해당 규칙이 맞지 않는 경우 swap을 통해서 재배치를 하여 조건에 만족하도록 배열을 만들어주는 알고리즘입니다. check와 up_and_down이라는 두개의 부울 변수를 이용해서 B[0] <= B[1] >= B[2] <= B[3] ... 를 만족할 수 있도록 만들어 줍니다. check 부울 변수는 해당에 안내를 해주는 변수로 True일 때는 B[i] <= B[i+1] 이 되어야 함을 알려주고, False일 때에는 B[i] >= B[i+1]이 되어야 함을 알려줍니다. up_and_down 변수는 배열의 현재상태를 알려주며, True일때에는 현재 배열의 상태가 A[i] <= A[i+1]이면 True, A[i] >= A[i+1] False값을 가집니다. 따라서 check 변수와 up_and_down 변수가 일치하면 배열상태를 유지하고 변수가 다르면 리스트 요소를 swap해 조건에 맞도록 배열을 재배열합니다. 
'''
'''
Big-O시간 : O(n)
solve함수는 0 원소부터 n-1번째원소까지 이동 하며 해당 규칙을 만족하지 않을 경우 swap이 일어나는 방식으로 오르락 내리락 규칙인 B[0] <= B[1] >= B[2] <= B[3] ... 을 구현합니다. 따라서 swap이 되는 경우 O(1)시간 걸리고 전체 for문이 n번 만큼 돌게 되므로 O(1)*n = O(n)만큼 시간이 걸립니다
'''

def solve(A):
	# return a list B such that B[0] <= B[1] >= B[2] <= B[3] ...
	# check 변수 초깃값 True(B[0]<=B[1]이어야함으로 True로 초기화)
	check = True
	# up_and_down 은 배열을 아직 확인하지 않았으므로, None으로 초기화
	up_and_down = None
	for i in range(len(A)-1):
		# 현재 배열이 어떤 상태인지 파악
		if A[i] > A[i+1]:#내려가는 경우 False
			up_and_down = False
		elif A[i] <= A[i+1]:#올라가는 경우 True
			up_and_down = True
		if check != up_and_down :
			A[i], A[i+1] = A[i+1],A[i]
		# 다음 배열의 안내를 위해 변수를 바꿔줌 
		check = not(check)
	return A

def check(B):
	if not (B[0] <= B[1]): return False
	for i in range(1, len(B)-1):
		if i%2 == 1 and not (B[i] >= B[i+1]):
			return False
		if i%2 == 0 and not (B[i] <= B[i+1]):
			return False
	return True		
	
A = [int(x) for x in input().split()]
B = solve(A)
print(check(B))