'''
알고리즘 설명 : 파이썬의 리스트를 이용해서 구간 최소 값을 찾을 수 있도록 구현 하였습니다. A에 n개의 원소가 주어졌을 때 i번째 k개의 구간의 최소 값보다 i+1번째 k개의 구간의 최소 값의 인덱스는 반드시 크게 됩니다. 이러한 특징을 활용해서 코드를 구현해 주었습니다. 해당 구간의 최소 값이 될 수 있는 후보군을 저장하는 min_interval이라는 빈 리스트를 선언해주었습니다. 그리고 A리스트를 순서대로 for루프를 이용해서 스캔하며 업데이트를 해주었습니다. A의 첫 번째 원소를 min_interval에 집어 넣고, A의 i번째 원소는 min_interval[-1]와 비교하여 min_interval[-1] > num[i]인 경우 min_interval[-1]은 더이상 최소 값 후보가 될 수 없으므로 min_interval[-1] <= num[i] 가 될 때까지 pop()하고 num[i]를 append()를 해주고, min_interval[-1] <= num[i]이면 이후 구간의 최소 값 후보가 될 수 있으므로 append해줍니다. 그리고 j라는 포인트 변수를 이용해서 k개의 구간을 스캔했을 경우 B리스트에 min_interval[j]를 추가하고, 만일 min_interval[j]가 다음 구간에서 빠지게 된다면, j+1을 해주어 다음 후보를 가르킬 수 있도록 변수를 조정하여 최솟값을 append할 수 있도록 합니다.
'''
'''
Big-O시간 : O(n)
처음 최소 값을 저장할 리스트, 포인터 변수, 출력값을 저장할 리스트는 모두 상수시간에 선언합니다. ( O(1))
그리고 이후 for문을 체크해보면 i=0인 케이스에서는 리스트의 맨뒤에 num[i]값을 append함으로 해당 케이스에서는 상수시간이 걸립니다. 문제는 이외의 경우 추가 해주는 것인데, 안에 while문에서 조건에 부합하지 않는 원소들을 pop()하고, 마지막에 append()해주는 경우가 있는데요. 이 부분에서는 최악의 경우를 가정하면 n개의 쌓여있는 리스트에서 pop()을 지속적으로 해주는 것인데, 이 때 리스트의 pop()함수는 파라미터가 없어 O(1)이게 되어 O(n)이 됩니다. 하지만 이 경우, 리스트에 n개의 원소가 쌓이지 위해서 pop함수가 진행되지 않고, append만 해주는 경우가 되므로 수행시간을 표현해주면 T(n) = (C1(n-1) + C2(n) )/ n [단, c1,c2는 상수]이 되고 이를 결국 Big-O로 표현해주면, O(C) = O(1)이 되어 최악의 케이스가 존재하는 경우에도 평균적으로 상수시간임을 보장하여 Amortized O(n)이 됨을 알 수 있습니다.
마지막으로 해당 for문에서 마지막 케이스에서 if i>=k-1케이스에서 출력 리스트에 최소값을 append하는 경우는 O(1), 포인터 변수를 바꾸는 것도 비교, 더하기 연산만 쓰였음으로 O(1)이 걸립니다. 
따라서 이 for문은 Amortized O(n)이 되고, 전체 함수도 O(n)이 됩니다. 
따라서 이 함수를 호출하여 실행하는 것이 전체 코드의 수행시간과 같기 때문에 O(n)이 전체 수행시간이 됩니다.
'''
# 출력 함수 : 리스트 길이 만큼 출력하므로 O(n)
def print_list(A):
	for element in A : 
		print(element, end=" ")
	
# 최소 값을 찾아줄 함수
def interval_list(num, n, k):
	# 최소 값과 최소 값 후보를 저장할 리스트 
	min_interval = []
	# 최소 값을 가르킬 포인터 변수
	j = 0
	# 출력값을 저장할 리스트
	ans = []
	for i in range(n):
		# 처음 원소를 넣을 경우 : O(1)
		if i == 0  : 
			min_interval.append(num[i])
		else :
			# 이전 min_interval 값보다 큰 원소는 이후에 후보가 될 수 있으므로 최소값 후보 리스트에 append()
			if min_interval[-1] <= num[i]:
				min_interval.append(num[i])
			else : 
				# min_interval[-1] > num[i] 인경우 min_interval[-1]은 더이상 최소 값 후보가 될 수 없으므로 
				# min_interval[-1] <= num[i] 가 될 때까지 pop()하고 업로드 
				while True: 
					if len(min_interval) == j :
						break
					if min_interval[-1] <= num[i]:
						break
					min_interval.pop()
				min_interval.append(num[i])
				
		# 구간의 길이가 k일 경우 ans에 현재 최소 값 업데이트 
		if i >= k-1 :
			ans.append(min_interval[j])
			# 다음 구간에서 최소 값이 바뀌는 경우를 고려해서 포인트 업데이트
			if num[i-k+1] == min_interval[j]:
				j+=1
	#ans 반환
	return ans
# 입력
n, k = tuple(map(int, input().split()))
num = list(map(int, input().split()))
# 출력
print_list(interval_list(num,n,k))
