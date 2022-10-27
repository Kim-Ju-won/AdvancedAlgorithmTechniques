'''
알고리즘 설명 : 이 알고리즘은 가장자리에 있는 좀비가 먼저 떨어진다는 점과 뚫고 지나간 거리가 방향을 바꿔서 간거리와 갔다는 아이디어를 통해 구현한 함수입니다. 자세히 설명해드리면 길이 6에 +3, -5와 같은 좀비가 있다고 가정을 해봅시다. 그럼 +3이 이동하는 좀비의 거리는 4라는 점에서 만나게 되므로 4까지이동하고 방향을 바꿔 0으로 나가게 됩니다.총 이동거리는 5입니다. 이와 같은 방식으로 -5 아이디의 좀비를 살펴보면 3의 이동거리를 갖게 됩니다. 그렇다면 이 경우 뚫고 지나갈 수 있다고 가정을 한다면 해당되는 +3좀비가 이동하는 거리는 3이되고, -5 좀비가 이동한 거리는 5가 됩니다. 즉, 두 경우를 살펴보면 번호는 다르나, 이동거리는 갖다는 것을 파악할 수 있습니다. 따라서 이 두가지 컨셉을 혼합하여 사용하는 것인데, 거리는 뚫고 지나가는 것을 가정하여 미리 구해주고, 오름차순으로 정렬하여 해당 방향으로 빠져나가는 아이디는 가장 바깥쪽에 있는 아이디라는 것(내부에 있는 아이디는 바깥쪽에 있는 아이디보다 먼저 떨어질 수 없습니다.)을 이용해서 k번째로 떨어지는 좀비를 찾아줍니다. 

Big-O 수행시간 분석 : O(nlogn)
이 코드는 크게 세 파트로 볼 수 있습니다. 해당 위치에서 통과하여 나갈때까지 필요한 거리를 계산하고 방향을 저장하는 for문, 그리고 거리의 크기대로 오름차순으로 정렬하는 리스트 내장함수 sort(), 마지막으로 k번째 떨어지는 좀비를 구하는 while문입니다. 
우선 거리를 계산하는 건 좀비의 길이인 n만큼 for루프를 반복합니다. 안에서는 append, 계산, 비교연산들이 쓰여 해당 루프문은 O(n)입니다. 그리고 정렬하는 내장함수 sort()는 O(nlogn)을 보장하게 때문에 해당 부분은 O(nlogn)입니다. 마지막으로 while루프문은 k번째 좀비가 떨어질 때가지 반복이 됩니다. k번째에서 k는 n번째가 가장 최악의 경우의 수이므로 해당 부분또한 최대 O(n)이 됩니다. 
정리하면 O(n)+O(nlogn)+O(n) = O(nlogn)으로 빅오수행시간을 분석할 수 있습니다.
'''
def new_result(n,L,k, zombie):
	dist =[]
	for i in range(n):
		# 좀비 아이디가 +이면 오른쪽으로 빠져나가는 길이를 구해줌
		if zombie[i][1] > 0 :
			# 거리와 방향을 튜플 형태로 저장 
			dist.append((L-zombie[i][0], +1))
		# 좀비 아이디가 -이면 왼쪽으로 빠져나가는 길이를 구해줌 
		elif zombie[i][1] < 0 :
			# 거리와 방향을 튜플 형태로 저장
			dist.append((zombie[i][0], -1))
	# 거리를 기준으로 정렬 
	# O(nlogn)
	dist.sort(key=lambda x:x[0])
	#print(dist)
	
	i = 0 
	fall_left = 0 # 왼쪽에서 떨어질 좀비를 찾는 포인터 변수
	fall_right = n-1 # 오른쪽에서 떨어질 좀비를 찾는 포인터 변수
	chosen = 0
	
	# 최대 n번째임으로 O(n)
	while i < k : 
		direction =  dist[i][1]
		if direction > 0 :
			chosen = zombie[fall_right][1]
			fall_right -= 1
		elif direction < 0 : 
			chosen = zombie[fall_left][1]
			fall_left += 1
		i+=1
	
	#거리가 같고 반대로 떨어지는 경우가 존재하는 경우 체크
	if dist[k-1][0] == dist[k][0]:
		direction = dist[k][1]
		if direction > 0 :
			chosen = min(chosen, zombie[fall_right][1])
			#print(chosen, end =" ")
		elif direction < 0 :
			chosen = min(chosen, zombie[fall_left][1])
			#print(chosen, end =" ")
	return chosen

# 입력 : n, L ,k
n, L, k = map(int, input().split())
zombie = []
for i in range(n):
    zombie.append(list(map(int, input().split())))
#출력
print(new_result(n,L,k, zombie))
'''
아래는 처음에 제출했던 코드입니다. 이 코드 또한 모두 정답처리 되었습니다.

알고리즘 설명:
이 알고리즘은 가장자리에 있는 좀비가 먼저 떨어진다는 점, 만나면 방향이 바뀐다는 점을 이용해 시뮬레이션 성능을 보완한 알고리즘입니다. 구체적으로 설명하면 알고리즘은 좀비의 수가 변화할때(떨어질 때) 그리고 좀비가 서로 만나 방향을 바꿀 때를 기점으로 시뮬레이션이 진행되는 방식으로 알고리즘을 구현해주었습니다. 
우선 좀비를 변수로 받은 다음 아이디를 통해 방향을 나타내는 방향 벡터값을 해당 좀비 아이디에 추가해주었습니다.(양수는 +, 음수는 -). 좀비는 가장자리에 있는 좀비가 먼저 떨어지므로, 각 가장자리에 있는 좀비가 가장자리쪽을 방향으로 이동할 때 필요한 시간을 계산해줍니다. 그리고 좀비가 떨어지기 이전에 서로 만날 수 있는 좀비가 서로 만나 방향을 바꾸는 경우가 있는지 해당 시간을 계산해줍니다. 그리고 그 시간들 중 가장 적게 걸린 시간을 이동시켜 위치를 확인하고, 떨어질 경우 해당 좀비를 떨어진 좀비명단(check리스트)에 저장을 하고, 방향이 바뀐 경우 방향을 가르키는 벡터의 방향을 바꿔주었습니다.
이런 방식으로 k번째로 떨어질 때까지 루프를 돌며 좀비를 관찰 한 뒤 check리스트에 k번째로 떨어진 좀비아이디를 반환하는 방식의 코드를 구현해주었다.

Big-O시간: 해당 알고리즘은 result(n,L,k,zombie)함수를 통해서 떨어진 좀비를 체크하게 됩니다. 해당 알고리즘은 1개의 큰for루프문과 한개와 다수의 for루프문을 포함한 큰 while문으로 구현하였습니다. 첫번째 for루프문에서는 방향을 정의하는 for루프문으로 해당 루프문은 좀비를 스캔하며 이루어지므로 O(n)입니다. 그리고 두번째 while문은 k번째 좀비가 떨어질 때까지 움직이는 시뮬레이션 부분입니다. k번째에서 최대가 될 수 있는 숫자는 n번째이고, 만나는 경우 최대의 경우도 c*n과 같은 꼴로 나타납니다.(c는 상수) 정리해서 해당 while문은 최대 O(n)만큼 반복하고 해당 while문안에 여러개의 O(n)크기의 for문을 갖고 있으므로 해당 while문의 빅오는 O(n^2)이 됩니다. 
따라서 최종 빅오 시간은 O(n)+O(n^2)이되어 O(n^2)이 Big-O시간이 됩니다.

def result(n,L,k, zombie):
	# 방향 변수(왼쪽 = minus, 오른쪽 = plus)
	minus = -1
	plus = 1
	
	# 해당 좀비 번호에 방향이 바뀔수 있으므로 방향을 다루는 변수를 추가해줍니다.
	# 해당 루프 Big-O : O(n)
	for i in range(n):
		if zombie[i][1] < 0 :
			zombie[i].append(minus)
		elif zombie[i][1] >  0 :
			zombie[i].append(plus)
	check = [] 
	# while문 자체는 질의로 주어진 k번째 좀비가 떨어질 때까지 진행됩니다. 
	# while문은 여러개의 O(n)크기의 for루프문을 갖고 있습니다. 
	# Big-O시간 : O(n^2)
	while(k>0):
		# 만나는 경우의 수 파악
		check_meet = zombie[0][2]
		meet = []
		# 좀비의 길이만큼 스캔하면서 체크 : O(n)
		for i in range(1,len(zombie)):
			if check_meet != zombie[i][2]:
				check_meet = zombie[i][2]
				if check_meet == minus:
					meet.append([zombie[i-1][0], zombie[i][0]])
		# 0에 가까운 번호 떨어지는데 필요한 거리 체크 
		fall0 = L
		if zombie[0][2] == minus : 
			fall0 = zombie[0][0] - 0
		# L에 가까운 번호 떨어지는데 필요한 거리 체크
		fallL = L
		if zombie[-1][2] == plus :
			fallL = L - zombie[-1][0]
		# 만나는 경우 필요한 거리 체크
		meetcase=L
		for i in range(len(meet)):
			if ((meet[i][1] - meet[i][0])//2) < meetcase :
				meetcase =  (meet[i][1] - meet[i][0]) // 2

		# 세가지 수중 가장 숫자가 작은 케이스 이동 
		# move의 거리만큼 모든 좀비가 이동하기 때문에 : O(n)
		move = min(fall0, fallL, meetcase)
		for i in range(len(zombie)):
			if zombie[i][2] == minus :
				zombie[i][0] -=move
			elif zombie[i][2] == plus :
				zombie[i][0] += move
		
		# 떨어지는 경우
		if zombie[0][0] == 0 or zombie[-1][0] == L:
			if zombie[0][0] == 0 and zombie[-1][0] == L: # 가장자리 두 좀비가 함께 떨어지는 경우
				if zombie[0][1] < zombie[0][1]:
					check.append(zombie[0][1])
					check.append(zombie[-1][1])
					zombie.pop(0)
					zombie.pop()
					k-=2
				elif zombie[0][1] > zombie[-1][1]:
					check.append(zombie[-1][1])
					check.append(zombie[0][1])
					zombie.pop()
					zombie.pop(0)
					k-=2
			# 좀비중 한마리만 떨어질 경우
			if zombie[0][0] == 0: 
				check.append(zombie[0][1])
				zombie.pop(0)
				k-=1
			elif zombie[-1][0] == L:
				check.append(zombie[-1][1])
				zombie.pop(-1)
				k-=1
				
		# 해당 조건문이 참일 경우 좀비의 길이만큼 루프문으로 돌게 됨. 
		if move == meetcase : # 만날경우 방향을 바꾸고 단위시간 1 만큼 이동
			change = False
			for i in range(len(zombie)):
				if i != 0 and zombie[i][2] == minus and zombie[i-1][2] == plus and change == False: #방향 전환
					if zombie[i][0] == zombie[i-1][0]:
						zombie[i][2] = -zombie[i][2]
						zombie[i-1][2] = -zombie[i-1][2]

						if zombie[i][2] == minus :
							zombie[i][0] -= 1
						elif zombie[i][2] == plus :
							zombie[i][0] += 1

						if zombie[i-1][2] == minus :
							zombie[i-1][0] -=1
						elif zombie[i-1][2] == plus :
							zombie[i-1][0] += 1
						change = True
					else:
						if zombie[i][0] - zombie[i-1][0] == 1: 
							zombie[i][2] = -zombie[i][2]
							zombie[i-1][2] = -zombie[i-1][2]
							change = True
						else : 
							zombie[i][0] -=1
							zombie[i-1][0] +=1
							change = False
				else: # 만나지 않을 경우 1시간 만큼 이동
					if not(i != len(zombie)-1 and zombie[i][2] == plus and zombie[i+1][2] == minus):
						if zombie[i][2] == minus :
							zombie[i][0] -=1
						elif zombie[i][2] == plus :
							zombie[i][0] += 1
					change = False

				#단위시간 1만큼 움직인 후 떨어진 좀비 확인
				if zombie[0][0] == 0 or zombie[-1][0] == L:
					if zombie[0][0] == 0 and zombie[-1][0] == L: # 둘이 같이 떨어진 경우
						if zombie[0][1] < zombie[-1][1]:
							check.append(zombie[0][1])
							check.append(zombie[-1][1])
							zombie.pop(0)
							zombie.pop()
							k-=2
						elif zombie[0][1] > zombie[-1][1]: # 둘이 같이 떨어진 경우 
							check.append(zombie[-1][1])
							check.append(zombie[0][1])
							zombie.pop()
							zombie.pop(0)
							k-=2
						if zombie[0][0] == 0: # 하나의 좀비만 떨어진 경우
							check.append(zombie[0][1])
							zombie.pop(0)
							k-=1
						elif zombie[-1][0] == L: # 하나의 좀비만 떨어진 경우
							check.append(zombie[-1][1])
							zombie.pop()
							k-=1

	return check[k-1]

# 입력 : n, L ,k
n, L, k = tuple(map(int, input().split()))
zombie = []
for i in range(n):
	zombie.append(list(map(int, input().split())))
#출력
print(result(n,L,k, zombie))'''