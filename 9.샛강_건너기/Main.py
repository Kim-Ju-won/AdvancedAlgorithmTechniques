'''
알고리즘 설명: 이진 탐색을 이용한 알고리즘입니다. 0~L사이의 거리를 필요한 점프 값이 최대가 되도록 하는 길이로 간주하고 해당 길이가 되도록 제거하는 k개의 돌의 수를 찾는 방식으로 이진 탐색을 진행합니다. 따라서 두 개의 함수를 세워 알고리즘을 구현하였는데요, 하나는 0~L사이의 거리를 필요한 점프 값에서 진행하는 이진 탐색을 하는 부분이고, 다른 하나는 임의의 점프 길이가 되도록 빼줘야하는 돌의 수를 세주는 함수입니다. 
- check_min_jum : 0~L사이로 이진 탐색을 하는 함수입니다. 0~L사이로 둔 이유는 모든 돌을 제거하였을때 강의 폭만큼 점프 값이 필요하므로 L을 최대로 설정하였습니다. 그리고 이 안에서 이진 탐색을 진행하는데요. 우선 0~L사이의 중간값을 standard라고 한다면, 필요한 점프값이 standard일 때 얼마나 많은 점프수가 필요한지 check_bridge함수를 호출해서 계산해줍니다. 그리고 필요한 점프수가 k보다 클 경우 범위를 제거될 바위수가 줄어드어야 함을 의미함으로 맨끝값을 standard -1로 조정해주어 해당구간을 반으로 줄이고, 만약 이 반대의 경우(작거나 같은 경우)해당 시작구간을 standard+1로 조절하여 반으로 줄여주고, 이 때의 필요한 점프 값을 저장합니다. 
- check_bridge : 징검다리 돌을 스캔하며 두 개의 돌의 거리를 계산하여 standard보다 작을 경우, 해당 돌을 빼주야 하는 경우이므로 제거할 돌을 세주고, 커지는 경우 더이상 두개의 돌 사이에 제거할 돌이 없으므로 다음 구간을 설정하여 제거할 돌을 계산할 수 있도록 업데이트 해줍니다. 

Big-O 설명 : O(nlogL)
이 알고리즘은 두개를 고려해야합니다. 첫번째로는 제거할 돌의 수를 세주는 check_bridge함수, 두번째로는 이진탐색을 하는 부분입니다. 
첫 번째 함수는 check_bridge돌을 세주는 함수입니다. 해당 함수는 돌리스트를 순환하며 해당하는 제거할 돌을 세주는 함수입니다. for루프문을 돌면서 구현하고 안에서는 상수번의 비교만 이루어지므로 O(n)입니다. 
두 번째 함수는 check_min_jump인 이진 탐색함수입니다. while문을 이용해서 이진탐색을 구현하고 있습니다. 이 while문은 구간이 점차적으로 L, L/2, L/4, ... 순으로 줄어듧니다. 또한 각 경우마다 제거할 돌을 세줄 수 있도록 각 check_bridge함수를 호출 하고 있므르로 점화식으로 표현한다면 T(L) = T(L/2) + O(n)이되고 해당되는 점화식을 풀어주면 Big-O시간은 O(logL * n)으로 나타낼 수 있으므로 최종 빅오시간은 O(logL*n)이 됩니다. 
'''
def check_bridge(dol, standard,n) :
	count = 0 # 제거할 돌의 수
	check = 0 # 기준이 되는 돌
	# O(n) : 돌을 순서대로 스캔하며 거리를 재며 제거할 돌을 세줌
	for i in range(n+1):
		# 길이가 standard보다 크므로 기준이 되는 돌 업데이트
		if dol[i] - check >= standard:
			check = dol[i]
		# standard보다 작은 경우 해당돌은 제거해야하는 것임을 의미하므로 갯수를 세준다.
		else : 
			count +=1
	return count

def check_min_jump(L,n,k,dol): 
	max_need_jump = 0
	start = 0
	last = L
	# O(logL * n)
	# 0~L구간을 이진탐색하면서 체크함
	while start <= last : 
		standard = (start+last)//2
		min_jump = check_bridge(dol, standard, n) # 제거할 돌의 수를 세주는 함수 O(n)
		# 점프수가 k보다 클 때 
		if  min_jump > k :
			last = standard -1# 구간을 반으로 줄임
		# 점프수가 k보다 작을 때 
		else:
			start = standard + 1 #구간을 반으로 줄임
			max_need_jump = standard
	return max_need_jump
	
#입력
L, n, k = tuple(map(int, input().split()))
dol = list(map(int,input().split()))
dol.append(L)
#출력 
print(check_min_jump(L,n,k,dol))