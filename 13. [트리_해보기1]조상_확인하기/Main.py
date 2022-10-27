'''
알고리즘 : 이 알고리즘은 DFS함수를 통해 preorder, postorder 방문을 하여 방문 시간을 해당 preorder리스트와 postorder리스트에 저장해 놓는 전처리를 진행합니다. 그 이후 count_ancestor함수를 이용해서 query_ancestor라는 함수를 호출하여 각 query에서 true가 나오는 횟수(u가 v의 조상인 횟수)를 반환합니다. count_ancestor함수에서 호출하는 query_ancestor함수는 조건문을 통해 preoder 리스트에서 u의 인덱스 < v의 인덱스,postorder 리스트에서 u의 인덱스 > v의 인덱스 두가지를 만족할 때 True를 반환하도록 구현해주었습니다. 
정리하면 DFS전처리를 통해 preorder, postorder 시간을 리스트에 저장하는 전처리를 진행한 뒤, 해당 인덱스의 대소 비교를 통해 각 쿼리가 true인 경우(u가 v의 조상인 경우) true를 반환하고 true인 갯수를 세주는 방식으로 알고리즘을 구현하였습니다. 

Big-O 수행시간 : O(n)
입력할 때 tree의 자식노드를 알려주는 이차원리스트를 구현하는 과정에서 O(n)번이 걸렸고, 이후 q 입력을 받아 저장하는데 O(q)가 걸려 입력받은 값을 저장할 때 O(q)+O(n)= O(n)이 걸렸습니다. 
두번째로는 전처리하는 부분입니다. 해당 부분은 가장 상위에 있는 노드부터 DFS 방문을 통해서 두가지의 preorder, postorder리스트를 구현하고 있으므로 총 O(n)방문하게 됩니다. 따라서 전처리과정에서 걸리는 수행시간은 O(n)입니다.
마지막으로는 query를 저리하는 부분입니다. query를 처리하는 부분은 count_ancestors함수인데 , 각 쿼리문의 true,false를 판단하는 query_ancestors함수에서는 전처리된 리스트를 상수번 비교하므로, 각 쿼리문마다 O(1)이 걸리고, 최종적으로 query_ancestors함수를 for루프를 통해 q번 호출하고 있으므로 O(1)*q = O(q)가 됩니다. 
따라서 입력 - 전처리 - 쿼리를 처리하는 세가지 부분을 볼 때 O(n)+O(n)+O(q)이 되고 q의 최대 범위가 n의 최대범위보다 작으므로(문제조건) 총 O(n)이 걸린다고 볼 수 있습니다. 
'''
import sys
sys.setrecursionlimit(7000)
# O(n) : n개의 노드들을 재귀적으로 방문하므로 n번 방문
def DFS(ancestor,tree,preorder,postorder,mark):
	global current_pre # 전역으로 변수 사용
	global current_post
	mark[ancestor] = True # 방문을 한 경우 True로 check
	preorder[ancestor] = current_pre # Preorder 순서 저장
	current_pre += 1
	for child in tree[ancestor]:
		if mark[child] != True :
			DFS(child,tree,preorder,postorder,mark)
	postorder[ancestor]=current_post # Postorder 순서 저장
	current_post +=1

	
# O(1)
def query_ancestors (preorder,postorder, query) : 
	u, v = query
	# 자기 자신을 ancester라고 물었을때 
	if u == v : 
		return True
	# 질문 query가 u 또는 v의 범위가 노드의 수를 벗어났을 때 
	if u > n or v > n : 
		return False
	
	judge_pre = False
	if preorder[u] < preorder[v] : # preoder 리스트에서 u의 인덱스 < v의 인덱스
		judge_pre = True
	judge_post = False 
	if postorder[u] > postorder[v]: # postorder 리스트에서 u의 인덱스 > v의 인덱스
		judge_post = True
		
	if (judge_pre == True) and (judge_post == True) : # 두가지 조건이 모두 만족할때 조상 노드로 True 반환
		return True
	else : # 하나라도 만족하지 못하면 조상노드가 아니므로 # False반환
		return False

# O(q)
def count_ancestors(preorder,postorder, queries):
	count = 0
	for query in queries : # O(q)
		q = query_ancestors(preorder,postorder,query) # 조상노드일 경우 True 반환 O(1)
		if q == True: # 조상노드일 경우 count 1 증가
			count+=1
	return count
# 1.입력 
n, q = tuple(map(int, input().split()))
# n개의 노드에서 자식노드를 가르키는 이차원 트리 리스트 선언
tree = [[] for i in range(n+1) ]

# O(n): n-1 개의 에지 정보를 입력 받아 해당 트리 구성
# for루프로 n-1개를 입력받아 list에 append를(O(1)) 하여 트리 리스트에 정보 추가 
edges = [ tuple(map(int, input().split())) for _ in range(n-1)] # O(n)
for edge in edges:
	p, c= edge
	tree[p].append(c)

# 2.전처리
# preorder와 postorder를 저장할 리스트 선언
preorder = [0]*(n+1)
postorder = [0]*(n+1)
mark = [False] * (n+1)
current_pre = 1
current_post = 1
DFS(1,tree,preorder,postorder,mark)
# O(q) : q개 만큼 입력을 받음 
queries = [ tuple(map(int, input().split())) for _ in range(q)]
# 3. 출력
# 출력 : O(q) => query 한개 수행시간 O(1) * query 갯수 = O(1)*q = O(q)
print(count_ancestors(preorder, postorder, queries))