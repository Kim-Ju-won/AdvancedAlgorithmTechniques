'''
알고리즘 설명 : max연산을 지원하는 MaxStack class를 만들어줍니다. MaxStack 클래스는 일반 원소를 저장하는stack의 역할을 하는 멤버변수 items와 max값을 저장하는 스택인 max_items라는 스택 멤버 변수를 만듭니다. push가 일어날 경우 멤버변수 items에 기본적으로 push가 되고, 만약 새로들어오는 value가 max_items의 top보다 같거나 큰 경우 max_items에도 push됩니다. 같거나 큰 경우로 둔 이유는, 만약 동일한 max값이 계속 들어왔을 때 push연산을 용이하게 하기 위해 같거나 같은 경우로 설정하였습니다. 이 경우 max_items에 가장 위에 있는 값이 stack에 저장되어 있는 값 중 가장 큰 max가 되고, max함수가 호출 될 때마다 max_items의 가장 top()의 위치에 있는 값이 반환됩니다. pop()이 일어날 경우 멤버변수 items에 맨 끝값이 pop이 되고, 만약 pop()이 되는 value가 max_items의 top보다 같을 경우 max_items에도 pop이 됩니다. 
'''
'''
Big-O시간 : 
- Stack class의 push, pop, top list의 내장함수 append, pop, []연산자를 사용했으므로 모두 상수시간에 마무리 됩니다.
- max연산자가 추가된 MaxStack 함수의 Big-O
#1. push : 멤버변수 items에 기본적으로 push가 되고, 만약 새로들어오는 value가 max_items의 top보다 같거나 큰 경우 max_items에도 push됩니다. 두 멤버 변수는 모두 stack push()함수를 이용했으므로 O(1)입니다.
#2. pop : 멤버변수 items에 맨 끝값이 pop이 되고, 만약 pop()이 되는 value가 max_items의 top보다 같을 경우 max_items에도 pop이 됩니다. 두 멤버 변수는 모두 stack의 pop()를 이용했으므로 O(1)입니다.
#3. max : max_items의 가장 위에 있는 값이 반환됩니다. stack의 top()함수를 이용했으므로 이 역시 Big-O시간은 O(1)입니다.
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

class MaxStack:
	def __init__(self): 
		self.items = Stack()
		self.max_items = Stack()
	
	# O(1)
	def push(self, value):
		self.items.push(value)
		if self.max_items:
			if self.max_items.top() <= value :
				self.max_items.push(value)
		else : #원소가 아예 없는 경우
			self.max_items.push(value)
	
	# O(1)
	def pop(self):
		if len(self.items) > 0 : # 원소가 있을 경우 
			value = self.items.pop()
			if value == self.max_items.top():
				self.max_items.pop()
			return value 
		else : #없을 경우 Empty 문구 반환
			return "EMPTY"
	
	#O(1)
	def max(self):
		if len(self.items) > 0 : # 원소가 있을 경우 
			return self.max_items.top()
		else : # 원소가 없을 경우 Empty 문구 반환
			return "EMPTY"

# s에 max연산이 추가된 stack에 
s = MaxStack()
# 입력창 : exit이 나오면 종료 
while True : 
	inst = input().split()
	if inst[0] == "pop":
		print(s.pop())
	elif inst[0] == "push":
		s.push(int(inst[1]))

	elif inst[0] == "max":
		print(s.max())
	elif inst[0] == "exit": #종료
		break
	else : # 명령어 이외의 명령어를 받으면 명령어를 다시 받음
		continue
		
		
		