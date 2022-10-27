'''
알고리즘 : 이 알고리즘은 DFS의 preorder, postorder 방식의 전처리와 diff를 이용한 BIT를 이용해 구현하였습니다. 우선 트리의 노드의 엣지 정보를 이용하여 이차원리스트로 트리를 구성해주고, cost를 입력받아 리스트형태로 저장합니다. 
이후 DFS 방식을 통해 preorder의 순서를 리스트에 저장하고 또한 preorder로 저장하는 동시에 해당 노드까지의 cost_sum도 path_sum배열에 저장합니다. update를 할 경우에 중복되어 부트리에 더해준 값을 빼줘야하므로 postorder방식을 이용하여 해당 순서에 따른 부트리수를 계산하여 count리스트에 저장해줍니다. 
그리고 이렇게 저장된 preorder리스트는 'preorder[인덱스] = 순서' 저장되어 있는데 BIT를 이용하기 위해 'preorder[순서]=트리 인덱스'형태로 저장해주고, cost, count, path_sum도 순서에 맞게 재배열 합니다. 
그리고 재배열된 path_sum을 이용하여 diff배열을 만들어주는데, path_sum[i]-path_sum[i-1]을 하여 diff[i]를 만들어줍니다. 이렇게 만들어진 diff를 이용하여 query_sum(i)가 주어질 경우 diff[0] + ... + diff[i]를 이용하여 구해줄 수 있습니다. 
BIT를 만들어주는데 모두 0인 리스트를 선언하고, 루프문을 돌며 update함수를 호출해, 해당 diff를 알맞은 위치에 더해줍니다. 이 떄 BIT는 1부터 n번째 인덱스까지 루프문을 돌며 update를 호출하여 오른쪽에 첫 번째 비트위치가 1인 인덱스가 update가 되는데, 이는 k와 k의 보수를 &연산을 통해 구해주는 LSB함수를 통해 구현해주었습니다.
BIT트리를 구성하는 전처리를 마무리 한 뒤에 query라는 함수를 호출하여 질의를 해결할 수 있도록 구현해주었습니다. query는 조건절을 이용하여 'sum'과 'update'를 구분하여 해당 명령에 알맞은 함수를 호출합니다.
'sum'는 query_sum함수를 호출하는데 query_sum는 diff[0]~diff[v]까지 더하는 함수로 BIT함수의 prefix_sum과 같은 형태로 구현해주었습니다.  prefix_sum은 BIT와 LSB함수를 이용하여 Log(n)번 안에 마무리 할 수 있도록 구현해주었습니다.
그리고 'update'부분은 BIT함수를 만들어줄 때 활용한 update함수를 2번 호출하여 문제를 해결할 수 있도록 구현해주었습니다. 2번 호출한 이유는 한번만 호출할 경우 해당 부트리에 update값이 추가로 더해져 최종 값이 다르게 나오지 않도록 하기 위함입니다. 미리 구해놓은 부트리의 수를 s라고 했을 때 update(BIT, v+s, -d)를 추가로 호출해주었습니다.

Big-O 수행시간 : O(nlogn)
이 함수는 크게 입력, DFS전처리, BIT전처리, Query문처리 4가지 순서로 빅오시간을 구해줄 수 있습니다.
입력은 for루프를 이용하여 n-1개의 엣지를 입력받아 이차원 트리를 구성하고, q개의 질의를 입력받습니다. 따라서 입력은 O(n)+O(q)로 나타낼 수 있고, O(n)의 최대범위가 크므로 O(n)이라고 볼 수 있습니다. 
다음은 DFS전처리 부분입니다. DFS전처리 함수는 재귀적으로 구성이 되어있는데, 궁극적으로 모든 노드를 방문하면 종료되므로 O(n)만큼 반복합니다. 해당 함수 안에서 이루어지는 preorder방식으로 로 구해주는 preorder_list와 path_sum 리스트와 그리고 postorder방식으로 부트리의 갯수를 세주는 count리스트를 구하는 부분은 으로 이루어져있습니다. 각각 노드의 값을 구해주는 시간은 상수시간이므로 전체 반복횟수인 n을 곱해 O(n)으로 나타낼수 있습니다. 
세번째로는 BIT전처리 부분입니다. BIT를 구성하기 앞서서 preorder, path_sum, count리스트가 BIT 구성에 맞도록 인덱스와 값의 위치를 바꾸는 과정에서 원소의 갯수만큼 반복하므로 O(n)이 걸립니다. 그리고 path_sum을 이용하여 인접한 노드의 값의 차이인 diff리스트의 값을 구해주는데 path_sum[i]-path_sum[i-1]를 루프문으로 n번 만큼 반복하므로 이 또한 O(n)이 걸립니다.이 diff리스트를 이용하여 BIT트리를 구현해줍니다. BIT트리는 update함수를 이용하는데 update함수는 LSB함수를 반복하여 호출합니다. LSB함수는 비트 연산만을 하고 있으므로 O(1)이라고 볼 수 있고, while문은 최대 logn만큼 반복하고 있으므로 O(logn)이라고 볼 수 있습니다. 노드의 수만큼 반복하여 update함수를 호출하고 있으므로 O(nlogn)이 됩니다. 따라서 O(n)+O(n)+O(nlogn)=O(nlogn)이라고 볼 수 있습니다. 
마지막으로는 query처리 부분입니다. 해당함수는 q번만큼 반복합니다. 그리고 이 함수에서는 질의를 처리해주기위해 update함수 그리고 sum을 구하는 함수를 호출합니다. sum함수는 prefix_sum과 같은 형태로 BIT를 이용하여 LSB함수를 최대 logn번 반복하고 있으므로 O(logn)이고, update하는 부분은 두번의 update함수를 호출하고 있는데 각각 logn번 방법하브로 O(2logn)이므로 전체 함수는 O(qlogn)이라고 볼 수 있습니다. 
따라서 최종적으로는 O(n)+O(n)+O(nlogn)+O(qlogn)=O(nlogn)이 됩니다. 
''' 
# O(n) : n개의 노드들을 재귀적으로 방문하므로 n번 방문
def DFS(ancestor,tree,preorder,path_sum,mark,count):
	global current_t # 전역변수 사용
	global cost_sum
	global tree_cost
	global sub_count # 부트리수
	mark[ancestor] = True # 방문을 한 경우 True로 check
	preorder[ancestor] = current_t
	current_t += 1
	cost_sum += tree_cost[ancestor]
	#자식노드로 들어가기전 해당 노드의 코스트를 더해줌
	path_sum[ancestor] = cost_sum
	sub_count=0 # 매 노드마다 subtree 갯수 초기화
	for child in tree[ancestor]:
		if mark[child] != True : 
			sub_count+=DFS(child,tree,preorder,path_sum,mark,count)
			cost_sum-=tree_cost[child] # 부모노드로 올라갈때 child의 cost 값 제외
			sub_count += 1
	# 자기자신 포함해서 갯수를 더함
	count[ancestor]=(sub_count+1)
	# 자기자신을 제외한 자기 자식노드의 갯수 반환
	return count[ancestor]-1
	
# O(1) 비트연산 - k의 오른쪽에서 첫번째 1이 되는 비트 위치 계산
def LSB(k):
	return k&-k
# query_sum : O(logn) => LSB(K)를 호출해서 더하게 되는데 LSB(k)는 처음나오는 1의 위치로 while문의 반복은 결국 logn을 넘지 못하게 된다. 따라서 logn이 최대 반복 횟수
def query_sum(BIT,k) : 
	ans = 0 
	while k >= 1:
		ans += BIT[k]
		k = k - LSB(k)
	print(ans)
		
# O(logn) : 최대로 가정할 경우 logn 번 while문이 더해지므로 O(logn)
def update(BIT, v, d):
	while v < len(BIT):
		BIT[v] += d
		v = v + LSB(v)

# O(qlogn)
def query(BIT, queries, count):
	for q in queries:
		q_list = q.split()
		x = int(q_list[1])
		v = preorder[x]
		if q_list[0] =="sum": # O(logn)
			query_sum(BIT,v)
		elif q_list[0]=="update": # O(2*logn) = O(logn)
			d = int(q_list[2])
			s = count_index[v]
			# v에 해당 값만큼 증가
			update(BIT, v, d) # O(logn)
			# v의 부트리에 증가가 반영되지 않도록 값을 빼줌
			update(BIT, v+s, -d) # O(logn)

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
# preorder를 저장할 list와 path_sum의 위치를 저장할 함수 선언
preorder = [0]*(n+1)
path_sum = [0]*(n+1)
count = [0]*(n+1)
mark = [False] * (n+1)
current_t = 1 # 방문 순서
cost_sum = 0 # subtree 갯수 count
DFS(1,tree,preorder,path_sum,mark,count) # O(n)
# preorder 가 현재 A[preorder순서] = index 순으로 나와있으므로 A[index] = preorder번호가 나오도록 정리
# index 순서에 맞게 path, count 배치또한 재배치
# O(n)
preorder_index = [0]*(n+1)
path_sum_index =[0]*(n+1)
count_index = [0]*(n+1)
for i in range(1,n+1):
	preorder_index[preorder[i]] = i
	count_index[preorder[i]] = count[i]
	path_sum_index[preorder[i]] = path_sum[i]
	
# diff 만들기 : path_sum_index의 인접한 값을 빼서 만들어줌
diff = [0] * (n+1)
for i in range(1,n+1):
	if i == 1 :
		diff[i] = path_sum_index[i]
	else : 
		diff[i] = path_sum_index[i]-path_sum_index[i-1]
# BIT 만들기 
# O(nlogn)
# cost에 있는 값을 update함수를 불러 T를 더해주며 업데이트를 시하여 Binary Indexed Tree 구현
# Update를 하기위해 LSB를 구하여 진행을 하는데 1이 나오는 횟수만큼 업데이트를 하게 됨
# 따라서 BIT의 BIT[k]는 k의 LSB 갯수 만큼 더해서 저장을 하게 되고 가장큰 k <= n이므로 각각의 update 연산은 O(logn)을 넘을 수 없음
# 따라서 n만큼 logn이 반복되므로 총 n*O(logn)=O(nlogn)
BIT = [0] * (n+1)
for i in range(1,n+1):
	update(BIT, i, diff[i])
# O(q) : q개 만큼 질의를 입력을 받음 
queries = [ input() for _ in range(q)]
# 3. 출력
# 출력 : O(q) => query 한개 수행시간 O(logn) * query 갯수 = O(logn)*q = O(qlogn)
query(BIT, queries, count)