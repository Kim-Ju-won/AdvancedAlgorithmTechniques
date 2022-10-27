'''
알고리즘 : 이 알고리즘은 DFS의 preorder, postorder 방식의 전처리와 BIT를 이용해 구현하였습니다. 우선 트리의 노드의 엣지 정보를 이용하여 이차원리스트로 트리를 구성해주고, cost를 입력받아 리스트형태로 저장합니다. 
이후 DFS 방식을 통해 preorder의 순서를 리스트에 저장하고 postorder방식을 이용하여 해당 순서에 따른 부트리수를 계산하여 저장해줍니다. 부트리의 수를 저장하는 이유는 부트리의 합을 출력할 때, preorder로 방문하게 되는 경우 해당 parent의 부트리가 부트리 수만큼 인접해서 나타나게 되는데 부트리의 수를 이용하므로써 간단하게 구간합을 구할 수 있기 때문입니다.
그리고 이렇게 저장된 preorder리스트는 'preorder[인덱스] = 순서' 저장되어 있는데 BIT를 이용하기 위해 'preorder[순서]=트리 인덱스'형태로 저장해주고, cost와 count도 순서에 맞게 재배열 합니다. 
그리고 BIT를 만들어주는데 모두 0인 리스트를 선언하고, 루프문을 돌며 update함수를 호출해, 해당 cost를 알맞은 위치에 더해줍니다. 이 떄 BIT는 1부터 n번째 인덱스까지 루프문을 돌며 update를 호출하여 오른쪽에 첫 번째 비트위치가 1인 인덱스가 update가 되는데, 이는 k와 k의 보수를 &연산을 통해 구해주는 LSB함수를 통해 구현해주었습니니다. 
BIT트리를 구성하는 전처리를 마무리 한 뒤에 query라는 함수를 호출하여 질의를 해결할 수 있도록 구현하였습니다. query는 조건절을 이용하여 'subtree'와 'update'를 구분하여 해당 명령에 알맞은 함수를 호출합니다.
'subtree'는 query_subtree함수를 호출하는데 query_subtree 함수는 부트리의 합이므로 미리 전처리해둔 부트리의 갯수를 저장해놓은 count리스트를 이용해서 부트리의 끝인덱스를 구해줍니다. 부트리의 끝인덱스까지의 prefix_sum과, 현재 v-1의 prefix_sum을 빼서 해당 질의를 해결해줍니다. prefix_sum은 BIT와 LSB함수를 이용하여 Log(n)번 안에 마무리 할 수 있도록 구현해주었습니다.
그리고 'update'부분은 BIT함수를 만들어줄 때 활용한 함수를 이용해 같은 방식으로 문제를 해결할 수 있도록 구현해주었습니다.

Big-O 수행시간 : O(nlogn)
이 함수는 크게 입력, DFS전처리, BIT전처리, Query문처리 4가지 순서로 빅오시간을 구해줄 수 있습니다.
입력은 for루프를 이용하여 n-1개의 엣지를 입력받아 이차원 트리를 구성하고, q개의 질의를 입력받습니다. 따라서 입력은 O(n)+O(q)로 나타낼 수 있고, O(n)의 최대범위가 크므로 O(n)이라고 볼 수 있습니다. 
다음은 DFS전처리 부분입니다. DFS전처리 함수는 재귀적으로 구성이 되어있는데, 궁극적으로 모든 노드를 방문하면 종료되므로 O(n)만큼 반복합니다. 해당 함수 안에서 이루어지는 preorder리스트와 부트리의 갯수를 세주는 count리스트를 구하는 부분은 각각 상수시간이므로 전체 반복횟수인 n을 곱해 O(n)으로 나타낼수 있습니다. 
세번째로는 BIT전처리 부분입니다. BIT를 구성하기 위해 preorder, cost, count리스트가 BIT 구성에 맞도록 인덱스와 값의 위치를 바꾸는 과정에서 원소의 갯수만큼 반복하므로 O(n)이 걸립니다. 그리고 BIT트리는 update함수를 이용하는데 update함수는 LSB함수를 반복하여 호출합니다. LSB함수는 비트 연산만을 하고 있으므로 O(1)이라고 볼 수 있고, while문은 최대 logn만큼 반복하고 있으므로 O(logn)이라고 볼 수 있습니다. 노드의 수만큼 반복하여 update함수를 호출하고 있으므로 O(nlogn)이 됩니다. 따라서 O(n)+O(nlogn)=O(nlogn)이라고 볼 수 있습니다. 
마지막으로는 query처리 부분입니다. 해당함수는 q번만큼 반복합니다. 그리고 이함수에서는 경우에 따라 update함수 그리고 subtree의 합을 구하는 함수를 호출합니다. update함수는 위에서 설명했듯이 logn이고, subtree함수는 두번의 prefix_sum함수를 호출하고 있는데 prefix_sum함수는 BIT를 이용하여 LSB함수를 최대 logn번 반복하고 있으므로 O(q * 2 logn) = O(qlogn)이라고 볼 수 있습니다. 
따라서 최종적으로는 O(n)+O(n)+O(nlogn)+O(qlogn)=O(nlogn)이 됩니다. 
'''
# O(n) : n개의 노드들을 재귀적으로 방문하므로 n번 방문
def DFS(ancestor,tree,preorder,count,mark):
	global current_t # 전역변수 사용
	global sub_count
	mark[ancestor] = True # 방문을 한 경우 True로 check
	preorder[ancestor] = current_t
	current_t += 1
	sub_count=0 # 매 노드마다 subtree 초기화
	for child in tree[ancestor]:
		if mark[child] != True : 
			# 자식노드가 늘어날 때마다 해당 자식노드의 수를 더해줌
			sub_count+=DFS(child,tree,preorder,count,mark)
			sub_count += 1
	# 자기자신 포함해서 갯수를 더함
	count[ancestor]=(sub_count+1)
	# 자기자신을 제외한 자기 자식노드의 갯수 반환
	return count[ancestor]-1 
	
# O(1) 비트연산 - k의 오른쪽에서 첫번째 1이 되는 비트 위치 계산
def LSB(k):
	return k&-k
# prefix_sum : O(logn) => LSB(K)를 호출해서 더하게 되는데 LSB(k)는 처음나오는 1의 위치로 while문의 반복은 결국 logn을 넘지 못하게 된다. 따라서 logn이 최대 반복 횟수
def prefix_sum(BIT, k):
	temp = 0 
	while k >= 1:
		temp += BIT[k]
		k = k - LSB(k)
	return temp

# O(logn) : prefix_sum함수 두번 호출하고 각각 logn번이 최대횟수이므로 logn
def query_subtree(BIT,v,count) : 
	u = count_index[v]+v-1
	ans = prefix_sum(BIT,u)-prefix_sum(BIT,v-1)
	print(ans)

# O(logn) : 최대로 가정할 경우 logn 번 while문이 더해지므로 O(logn)
def query_update(BIT, v, d):
	while v < len(BIT):
		BIT[v] += d
		v = v + LSB(v)

# O(qlogn)
def query(BIT, queries):
	for q in queries: # O(q)번 반복
		q_list = q.split()
		x = int(q_list[1])
		v = preorder[x]
		if q_list[0] =="subtree": # subtree연산을 위해 query_subtree함수 호출
			query_subtree(BIT,v,count) # O(logn)
		elif q_list[0]=="update":# update연산을 위해 query_update함수 호출
			d = int(q_list[2]) 
			query_update(BIT,v,d) # O(logn)
# 1.입력 
n, q = tuple(map(int, input().split()))
# 각 트리의 가격
tree_cost = [0]+list(map(int,input().split()))
# n개의 노드에서 자식노드를 가르키는 이차원 트리 리스트 선언
tree = [[] for i in range(n+1) ]
# O(n): n-1 개의 에지 정보를 입력 받아 해당 트리 구성
# for루프로 n-1개를 입력받아 list에 append를(O(1)) 하여 트리 리스트에 정보 추가 
edges = [ tuple(map(int, input().split())) for _ in range(n-1)] # O(n)
for edge in edges:
	p, c= edge
	tree[p].append(c)
# 2.전처리
# preorder를 저장할 list와 부트리의 갯수를 저장할 count 리스트 선언
preorder = [0]*(n+1)
count = [0]*(n+1)
mark = [False] * (n+1)
current_t = 1 # 방문 순서
sub_count = 0 # subtree 갯수 count
DFS(1,tree,preorder,count,mark) # O(n)
# preorder 가 현재 A[preorder순서] = index 순으로 나와있으므로 A[index] = preorder번호가 나오도록 정리
# index 순서에 맞게 count, cost 배치또한 재배치
# O(n)
preorder_index = [0]*(n+1)
cost_index = [0]*(n+1)
count_index =[0]*(n+1)
for i in range(1,n+1):
	preorder_index[preorder[i]] = i
	cost_index[preorder[i]] = tree_cost[i]
	count_index[preorder[i]] = count[i]
# BIT 만들기 
# O(nlogn)
# cost에 있는 값을 update함수를 불러 T를 더해주며 업데이트를 시하여 Binary Indexed Tree 구현
# Update를 하기위해 LSB를 구하여 진행을 하는데 1이 나오는 횟수만큼 업데이트를 하게 됨
# 따라서 BIT의 BIT[k]는 k의 LSB 갯수 만큼 더해서 저장을 하게 되고 가장큰 k <= n이므로 각각의 update 연산은 O(logn)을 넘을 수 없음
# 따라서 n만큼 logn이 반복되므로 총 n*O(logn)=O(nlogn)
BIT = [0] * (n+1)
for i in range(1,n+1):
	query_update(BIT, i, cost_index[i])

# O(q) : q개 만큼 질의를 입력을 받음 
queries = [ input() for _ in range(q)]
# 3. 출력
# 출력 : O(q) => query 한개 수행시간 O(logn) * query 갯수 = O(logn)*q = O(qlogn)
query(BIT, queries)