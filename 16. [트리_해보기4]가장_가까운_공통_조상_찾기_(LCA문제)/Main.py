'''
알고리즘 : 이 알고리즘은 DFS로 순회하면서 Euler tour 순서와 해당하는 순서에 해당하는 순서의 depth를 구해주는 전처리를 하였고, 이를 이용해서 LCA를 구해주는 알고리즘을 구현해주었습니다.
DFS 탐색을 하면서 Euler tour와 해당하는 tour의 depth를 리스트에 저장해주었습니다. DFS 탐색을 하며 저장한 방식은 다음과 같습니다. 첫번째로 방문했을 때 해당 노드의 번호를 euler 리스트에 append해두었고, 전역변수로 선언해둔 depth를 euler_depth라는 리스트에 append를 해두었습니다. 그리고 child노드를 방문할 때 DFS함수를 호출하기 전, 아래로 내려가므로 depth를 1증가 시켜주었고 해당 노드의 child를 방문하고 올라왔을 때 다시 방문한것과 같으므로 euler_tour리스트에 다시 한번 append를 시키고, 올라왔으므로 depth를 1 감소 시켜 저장해두었습니다. 
그리고 이 전처리된 euler_depth와 euler_tour리스트를 이용하여 LCA함수를 호출하여 query를 해결하도록 함수를 구현하였습니다. 이 함수는 다음과 같은 아이디어를 이용해 구현해주었습니다. 여기서 노드 u와 v의 lca는 반드시 배열 u와 v사이에 존재하게 됩니다. 그 이유는 해당 부분은 u에서 v로 이동하는 경로와 같기 때문에 반드시 lca가 그 사이에 존재하게 됩니다. 그리고 이 사이에 존재하는 노드들 중 가장 depth가 작은 노드가 lca노드가 됩니다. 따라서 쿼리로 주어진 원소 u, v를 이용하여 euler_tour의 리스트 중 해당 범위를 찾고 가장 작은 depth를 가지는 노드 번호를 반환하도록 구현해주었습니다. 
Big-O 수행시간 : O(n*q)
이 함수는 크게 입력하는 부분과 euler_tour, euler_depth전처리과정과 LCA함수를 호출하여 query를 해결하는 부분으로 나눠 볼 수 있습니다.
우선 입력은 입력은 for루프를 이용하여 n-1개의 엣지를 입력받아 이차원 트리를 구성하고, 루프문을 이요하여 q개의 질의를 입력받습니다. 따라서 입력은 O(n)+O(q)로 나타낼 수 있고, O(n)의 최대범위가 크므로 O(n)이라고 볼 수 있습니다. 
다음은 euler tour, depth를 구하는 과정입니다. 재귀적으로 DFS를 호출하는 방식으로 구현해주었는데, 방문하고 올라갈 때마다 append연산이 일어납니다. 따라서 2*n이 최대가 되며 따라서 O(n)임을 할 수 있습니다. 
다음은 LCA쿼리 처리 부분 함수입니다. 이 부분에서는 for루프를 이용해 q번 query연산을 진행합니다. 각 연산에서 u,v의 인덱스를 찾아 for루프를 돌며 해당 구간의 최소 depth를 찾아 해당 노드 번호를 반환해줍니다. 따라서 해당 루프문이 최대 n번 방문하는 것이 최악의 경우이므로 O(n*q)로 볼 수 있습니다. 
따라서 이 알고리즘은 O(n)+O(n)+O(n*q)=O(n*q)로 볼 수 있습니다.
'''
import sys
sys.setrecursionlimit(7000)

# O(n) : n개의 노드들을 재귀적으로 방문하므로 n번 방문
def DFS(ancestor,tree,mark,euler_tour,euler_depth):
	global depth # 전역으로 변수 사용
	mark[ancestor] = True # 방문을 한 경우 True로 check
	euler_tour.append(ancestor) # 방문할 때 위치 저장
	euler_depth.append(depth)
	for child in tree[ancestor]:
		if mark[child] != True :
			depth+=1 # 내려갈 때 depth +1
			DFS(child,tree,mark,euler_tour,euler_depth)
			euler_tour.append(ancestor) # 다시 올라갈 때 방문 번호 저장
			depth-=1 # 올라갈 때 depth -1
			euler_depth.append(depth) # 올라갈 때 방문 번호의 depth 저장
	

# O(q*n)
def LCA(euler_tour,euler_depth, queries):
	for query in queries: # q번 반복
		u, v = query
		p1 = euler_tour.index(u) # u가 나오는 인덱스 반환
		p2 = euler_tour.index(v) # v가 나오는 인덱스 반환
		lca = 0
		min_depth = len(euler_tour) 
		for i in range(min(p1,p2), max(p1,p2)+1): # 최악의 경우 끝점과 끝점이 되어 O(n)반복을 할수도 있음
			if euler_depth[i] < min_depth: # 깊이가 더 낮은 노드가 나올때마다 LCA 업데이트
				min_depth = euler_depth[i] 
				lca = euler_tour[i]
		print(lca) # 최종 LCA 출력
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
# euler_tour와 euler_depth를 저장할 리스트 선언
euler_tour = [] # tour 번호를 저장할 리스트
euler_depth = [] # depth를 저장할 리스트
mark = [0] * (n+1)
depth = 1
# O(n) => DFS 는 O(n)번 방문하며 euler_tour, euler_depth 저장
DFS(1,tree,mark,euler_tour,euler_depth)

queries = [ tuple(map(int, input().split())) for _ in range(q)]
LCA(euler_tour,euler_depth, queries)
#LCA_sparse_table(s_table, queries)

