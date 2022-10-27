#함수
def output(n, m, edges, array):
	check = n//2
	edge_y = dict()
	
	for i in range(m):
		key = edges[i][1]
		if key in edge_y:
			edge_y[key].append(edges[i][0])
		else : 
			edge_y[key] = [edges[i][0]]
	
	for key in edge_y.keys():
		edge_y[key].sort()
	#nlogn
	key_order = list(edge_y.keys())
	key_order.sort(reverse=True)
	
	for key in key_order:
		if check in edge_y[key] : 
			check+=1
		elif (check-1) in edge_y[key]:
			check-=1
	return array[check]
#입력
n, m = tuple(map(int, input().split()))
array = list(map(int, input().split()))
edges = [ tuple(map(int, input().split())) for _ in range(m)]
#출력
print(output(n, m, edges, array))