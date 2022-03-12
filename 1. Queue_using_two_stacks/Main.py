'''
알고리즘 설명 :  스택을 두개를 이용해서 만든 큐는 enqueue를 위한 스택 enq_stack과 그리고 dequeue를 위한 스택 deq_stack을 이용해서 구현합니다. enqueue는 enq_stack의 push함수를 이용해서 추가해줍니다. 여기서 중요한 점은 큐는 스택과 다르게 LIFO가 아닌 FIFO구조를 취하고 있는데, 이 부분은 남은 deq_stack을 이용해서 dequeue 함수를 구현함으로서 해당 문제점을 해결합니다. 먼저 deq_stack의 리스트가 비어있다면, enq_stack의 모든 원소를 pop을 시키는 동시에 deq_stack에 push해 줍니다. 이렇게 되면 가장 먼저 들어갔던 원소가 deq_stack에서는 가장 상단에, 가장 나중에 들어온 원소는 deq_stack에서 가장 아래에 존재하게 되어 deq_stack에서는 FIFO구조가 완성됩니다. 이후 deq_stack의 가장 상단에 있는 원소를 pop()을 하여 dequeue기능을 완성합니다. 이 때, Empty가 되는 경우는 enq_stack, deq_stack모두 비어 있을 때며, enq_stack에서 deq_stack으로 옮기는 경우는 FIFO가 될 수 있도록 반드시 deq_stack의 원소가 없을 때 진행해야합니다.
'''
'''
Big-O시간 : 
- Stack class의 push, pop, top list의 내장함수 append, pop, []연산자를 사용했으므로 모두 상수시간에 마무리 됩니다.
- 두 개의 stack을 이용한 queue의 Big-O시간
#1. enqueue : push는 stack의 push 를 이용하므로 기본적으로 O(1)만큼 시간복잡도가 걸린다.
#2. dequeue : dequeue를 진행할 경우 최악의 경우 원소를 enqueue가 n개 주어지고, dequeue가 한 번 주어져서 모든 원소를 enq_stack에서 deq_stack 으로 이동해야 함으로 O(n)이 됩니다. 하지만, 극단적인 경우를 제외하고,  예를 들어 enq가 k번 연속으로 들어오고, deq가 k번 된다고 가정한다면, 첫번 째 dequeue가 일어났을 때 k번 원소를 옮겨서 O(k)만큼 시간이 걸리지만, 이후 남은 dequeue연산에서는 더이상 원소를 옮길 필요 없이 상수시간만에 dequeue를 하게 됨으로 O(1)임을 보장받습니다. 이 예시의 평균적인 dequeue 시간 복잡도가 O(1)이됩니다. 따라서 평균적인 케이스를 고려하면 결과적으로 O(1)의 Big-O시간을 보장하게 된다.

'''
# stack class
class Stack : 
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
	
class Queue:
	def __init__(self):
		self.enq_stack = Stack()
		self.deq_stack = Stack()
		
	# O(1) : push는 stack의 push 를 이용하므로 기본적으로 O(1)만큼 시간복잡도가 걸린다.
	def enqueue(self, x):
		self.enq_stack.push(x)
	
	# O(1) : dequeue는 평균적으로 O(1)임을 보장함
	def dequeue(self):
		if len(self.deq_stack) == 0 :
			if len(self.enq_stack) == 0 :
				return "EMPTY"
			else : 
				while len(self.enq_stack) != 0 : 
					self.deq_stack.push(self.enq_stack.pop())
		return self.deq_stack.pop()

# q 에 자료구조 queue객체 할당
q = Queue()
while True : 
	inst = input().split()
	if inst[0] == "deq":
		print(q.dequeue())
	elif inst[0] == "enq":
		q.enqueue(int(inst[1]))
	elif inst[0] == "exit": #종료
		break
	else : # 명령어 이외의 명령어를 받으면 명령어를 다시 받음
		continue