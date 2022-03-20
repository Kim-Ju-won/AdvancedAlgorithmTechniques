'''
알고리즘 설명 : 스택과 리스트 두개를 이용해서 알고리즘을 구현해주었습니다. 스택 자료구조는 파이썬의 리스트 함수를 이용해서 구현해주었습니다. 리스트 A와 stack를 이용해서 각 A[i]의 왼쪽에 있으며 작은 값중 가장 가까운 위치의 수를 찾는 알고리즘 인데요, 다음과 같이 진행합니다. 우선 리스트 A를 순서대로 스캔하면서 리스트의 원소를 조건을 걸어 stack에 push하고 pop()을 하는 과정동안 stack의 맨위의 원소를 정답을 나타내는 리스트인 B에 추가를 하는 방식으로 함수를 구현해주었습니다. 첫번째 원소를 넣을 때는 왼쪽에 값이 없으므로, 0을 추가하고, stack에 push해줍니다. 이 후, stack의 맨위의 원소와 A[i]의 원소를 비교하는데, stack.top() >= A[i] 인 경우, stack에서 A[i]보다 작은 값이 있는지 pop을 하며 확인해주고, 작은 값을 찾으면 해당하는 값을 B에 append하고, 없는 경우 0을 B에 append합니다. 만약 stack.top() < A[i] 경우 A[i]왼쪽에 작으며 가장 가까운 수를 바로 발견한 것이므로 B에 append해줍니다. 해당 연산이 마무리 된다음 stack에 A[i]를 push해주어, 다음 A[i+1]값과 비교할 수 있도록 세팅을 해줍니다.
'''
'''
Big-O시간 : O(n) 
이 알고리즘의 수행시간을 알기위해서는 Stack의 수행시간과 해당 함수인 check_left_min함수의 수행시간을 알아야합니다. 
- Stack 수행 시간 : 
# push 함수 : O(1)만큼 수행시간이 걸립니다. 리스트의 append함수를 활용했으므로 O(1)이 됩니다. 
# pop 함수 : O(1)만큼 빅오 수행시간이 걸립니다. 리스트의 pop()함수를 이용하고, parameter가 없으므로 O(1)이 됩니다.
# top 함수 : O(1)만큼 빅오 수행ㅇ시간이 걸립니다. 리스트의 맨위의 원소를 인덱스를 이용해서 상수시간 만에 접근하여 O(1)입니다.
- check_left_min 수행시간 : 
빈 스택과 출력할 값들을 저장할 빈 리스트를 선언합니다.(변수선언 상수시간) 
해당 함수의 Big-O부분을 구하기 위해 체크할 부분은 알고리즘이 돌아가는 for문인데요 케이스별로 분석하도록 하겠습니다. 우선 이 과정에서 stack에 첫 원소를 넣을 때는 push()연산, 리스트 append연산만 쓰이므로 O(1)이고, stack.top() < A[i]에도 push연산, 리스트 append 연산만 쓰이므로 O(1) 즉, 상수 시간만큼 걸립니다. 문제가 되는 부분은 stack.top() >= A[i] 경우인데, 최악의 경우를 가정한다고하면 해당 케이스에서 stack에 n개의 원소가 쌓있고, stack의 크기가 0이 될 때까지 pop을 반복해줘 해당 케이스의 최악의 경우에는 O(n)이 걸립니다. 하지만 이 경우에 전체 for문을 생각해보면 n개의 원소가 쌓이기 위해서는 n-1번의 상수시간동안 stack에서 pop이 되지 않고, 쌓아두게되므로 해당 경우를 제외한 n-1번동안은 O(1)의 상수 번의 push가 일어나게 됩니다. 그럼 전체 배열을 스캔하는 동안 이루어지는 횟수가 n이라고 한다면 전체 수행시간 T(n) = (C1(n-1) + C2(n) )/ n [단, c1,c2는 상수]이 되고 이를 결국 Big-O로 표현해주면, O(C) = O(1)이 되어 최악의 케이스가 존재하는 경우에도 평균적으로 상수시간임을 보장하여 Amortized O(n)이 됨을 알 수 있습니다.
따라서 이 코드는 함수를 부르고 출력을 하게 되어있으므로 함수 수행시간 O(n), 출력하는 시간O(n) 으로 전체 코드는 O(n)+O(n)이되어 전체코드는 O(n)이 됩니다.
'''
# Stack 클래스를 리스트를 이용해 구현
class Stack:
	def __init__(self):
		self.items = []
	
	#O(1) : 리스트의 append() 내장 함수를 이용했으므로 O(1)
	def push(self, value): 
		self.items.append(value)
	
	#O(1) : 리스트 pop() 함수에 파라미터가 없으므로 O(1)
	def pop(self):
		if len(self) > 0:# 원소가 있는 경우
			return self.items.pop()
		else : # 없는 경우 None 반환
			return None
	# O(1) : 맨 위의 아이템을 인덱스로 접근해서 받으므로 O(1)
	def top(self):
		if len(self) > 0 :
			return self.items[-1]
		else : # 없는 경우 None 반환
			return None 
		
	def __len__(self):
		return len(self.items)

def check_left_min(n, num):
	# 가까우면서 왼쪽에 있는 리스트 중 가장 가까운 수를 반환하는 배열
	answer = []
	# 입력으로 받은 리스트를 스캔하며, stack에 제일 나중에 들어온 top값과 비교하며 정답을 구해줌
	stack = Stack()
	
	# O(n) : 리스트에 있는 전체 원소를 넣고 빼는 과정을 거치게 되기 때문에 O(n)
	for i in range(n):
		# 첫 원소가 들어오는 경우 
		if stack.top() == None : 
			answer.append(0)
			stack.push(num[i])
		
		# stack의 맨위의 원소보다 num[i]보다 큰 경우 스택 아래로 내려가면서 처음으로 num[i]보다 작아지는 숫자를 반환
		elif stack.top() >= num[i]:
			
			# 원소의 길이가 0이되거나 num[i]보다 작은 값을 발견할 경우 루프 종료
			while True:
				if len(stack) == 0 : 
					break
				if stack.top() < num[i]:
					break
				stack.pop()
			
			if len(stack) != 0 : # 처음으로 작은 원소를 저장
				answer.append(stack.top())
			else : 
				answer.append(0) # 발견하지 못한 경우, 0 추가
			stack.push(num[i]) # 다음 비교를 위해 스택에 원소 추가
		
		# num[i]바로 이전 숫자가 더 작은 경우
		elif stack.top() < num[i]:
			answer.append(stack.top())
			stack.push(num[i])
			
	return answer

# 리스트 A를 프린트 하는 함수 O(n)
def print_list(A):
	for element in A : 
		print(element, end=" ")
# 입력
n = int(input())
num = list(map(int, input().split()))
# 출력
print_list(check_left_min(n, num))