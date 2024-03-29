'''
알고리즘 설명 : 이 알고리즘은 Dynamic Programming을 이용한 알고리즘입니다. 알고리즘의 작동원리는 다음과 같습니다. DP테이블을 선언하여 정해진 시간 t을 기준으로 하여 t가 0~t분 사이일 때 각 t분마다 먹을 수 있는 최대의 치킨의 갯수와 최고 남은 시간의 수를 차례로 저장합니다. DP[t]에 저장할 수 있는 기준은 "가장 적은 시간 맥주를 마시면서(가장 적은 남는 시간을 만드면서) 그 때에 가장 많이 먹을 수 있는 치킨의 수"를 저장하는 것입니다. 해당 기준에 대해서 대소 비교를 할 수 있도록 max_chicken함수를 통해서 이를 구현해주었습니다. 그리고 0~t사이의 수를 i라고 했을 때 DP[i]가 될 수 있는 후보군들은 다음과 같습니다. 

1) DP[i-1]에서 1분이 늘어난 경우, 먹은 치킨의 갯수가 유지되고, 남은 시간이 1분 늘어남
2) DP[i-a]에서 a분 늘어난 경우, DP[i-a]에서 먹은 치킨의 갯수가 1이 증가하고, 남은 시간이 유지됨
2) DP[i-b]에서 b분 늘어난 경우, DP[i-b]에서 먹은 치킨의 갯수가 1이 증가하고, 남은 시간이 유지됨

총 세가지 경우를 max_chicken 함수의 입력값으로 넘겨 DP테이블을 차례대로 채워주었습니다. 
코드에 대한 자세한 설명은 아래 주석을 참고하시면 됩니다.

Big-O시간 : O(t)
이 알고리즘은 solve함수와 max_chicken함수의 빅오시간을 분석하므로써 전체 알고리즘의 수행시간을 계산할 수 있습니다. 
우선 solve함수을 분석하면 solve함수는 입력 값이나 변수선언하는 부분은 상수시간안에 마무리 됩니다. 그리고 핵심적인 부분은 for루프을 0~t까지 돌면서 케이스에 따라 max_chicken함수를 호출하여 DP테이블을 채워나갑니다. max_chicken함수를 살펴보시면 입력으로 받은 리스트의 길이만큼 for루프를 돌며, 비교연산 및 대입연산을 진행하므로 for루프의 길이가 전체 빅오 시간을 결정하게 됩니다. 이 때 solve에서 넘겨주는 리스트의 길이는 2-3으로 고정되어 있는 것을 알 수 있으므로 여기서 호출되는 max_chicken의 최대 빅오시간은 O(3)=>O(1)로 상수시간이 됨을 알 수 있습니다. 
따라서 전체 for루프는 O(1)*t = O(t)로 O(t)만큼 돌고 있음을 알 수 있으며 이 Big-O시간이 알고리즘의 Big-O수행시간이 됩니다. 따라서 전체 알고리즘의 수행시간은 O(t)입니다.
'''
# max_cheicken함수의 설명
# cases의 크기 만큼 max_chicken은 방문합니다. 
# 이 알고리즘에서는 DP테이블을 완성하기 위한 함수로 최대 세개의 원소를 for루프로 비교하기 때문에 상수시간이 걸립니다. 
# for루프 내부의 연산은 비교연산과 대입연산으로 모두 상수시간만에 해결할 수 있습니다.
# Big-O시간 => O(3) = O(1)
# 이 함수의 작동원리는 남은 시간 t가 제일 작을 때, t와 먹은 치킨의 갯수를 업데이트하게 되며, 
# t가 같을 경우 제일 많이 먹을 수 있는 치킨의 갯수를 반환하개 됩니다.
def max_chicken(cases):
	# 남은 시간 :min_t, 최대 먹을 수 있는 치킨의 수: max_num
	min_t = 10001
	max_num = -1
	# 입력으로 받은 리스트를 for문을 돌며 연산을 진행합니다. 
	# 리스트의 길이는 2~3으로 호출할 때 길이가 고정됩니다. 
	# for문 내에서 진행하는 것은 비교연산, 대입연산이 상수번만 진행되므로 O(1)이라고 볼 수 있습니다.
	for case in cases : 
		# 치킨을 더 오랫동안 먹었을 때 (더 적은 시간이 남았을 떄)
		if case[1] < min_t :
			min_t = case[1]
			max_num = case[0]
		# 만약 치킨을 먹고 같은 시간이 남았을 때
		elif case[1] == min_t : 
			# 더 많이 먹은 치킨의 갯수로 업데이트
			if case[0] > max_num : 
				max_num = case[0]
	return [max_num, min_t]

# O(t) 
# for루프를 t분만큼 돌며 max_chicken함수를 호출하여 DP테이블을 채워 나갑니다. 
# max_chicken의 입력 매개변수로 넘기는 입력값은 2~3으로 고정되어 있습니다. 
# 이외의 for문에서 비교연산 및 대입연산이 상수번 일어납니다. 
# 따라서 O(t)라고 해당 함수는 Big-O시간을 볼 수 있습니다. 
def solve(a, b, t):
	# [먹은 치킨의 갯수, 남는 시간 ]을 원소로 하는 (t+1)길리의 DP테이블을 선언
	chicken_DP = [[0,0]] * (t+1) 
	minimum = min(a,b) # 1개를 먹을 때 더 적게 걸리는 시간
	maximum = max(a,b) # 1개를 먹을 때 더 많이 걸리는 필요한 시간
	# 빅오시간
	for i in range(1,t+1):
		# 초기화 : 치킨을 먹는 시간이 a,b분이므로 해당 구간 미만 구간에서는 치킨은 먹을 수 없고 맥주를 마시는 시간만 늘어남
		# 따라서 해당 구간에는 남는 시간이 1씩 증가 되도록 초기화
		if i < minimum and i <maximum: 
			chicken_DP[i] = [chicken_DP[i-1][0],chicken_DP[i-1][1]+1]
		# i가 a와 b사이에 있는 경우, 인덱스 에러가 나지 않도록 더 작은 값만 인덱스에서 빼서 max_chicken함수 호출
		elif i > minimum and i < maximum : 
			chicken_DP[i] = max_chicken([[chicken_DP[t-minimum][0]+1,chicken_DP[i-minimum][1]], 
																	[chicken_DP[i-1][0],chicken_DP[i-1][1]+1]])
		# i > a, i >b인 경우, DP[i]의 다음과 같이 후보를 세개로 나눌 수 있음 
		# 1) DP[i-1]에서 1분이 늘어난 경우, 먹은 치킨의 갯수가 유지되고, 남은 시간이 1분 늘어남
		# 2) DP[i-a]에서 a분 늘어난 경우, DP[i-a]에서 먹은 치킨의 갯수가 1이 증가하고, 남은 시간이 유지됨
		# 2) DP[i-b]에서 b분 늘어난 경우, DP[i-b]에서 먹은 치킨의 갯수가 1이 증가하고, 남은 시간이 유지됨
		# max_chicken함수를 호출하여 규칙에 맞게 가장 적게 남는 시간과 그 상황에서 가장 많이 먹은 치킨의 갯수를 저장
		else : 
			chicken_DP[i] = max_chicken([[chicken_DP[i-a][0]+1,chicken_DP[i-a][1]], 
																	[chicken_DP[i-b][0]+1,chicken_DP[i-b][1]],
																	[chicken_DP[i-1][0],chicken_DP[i-1][1]+1]])
	# DP테이블이 t분일 때 해당 경우의 치킨의 갯수, 및 남는 시간 출력
	# 남는 시간이 없는 경우
	if chicken_DP[t][1] ==0:
		print(chicken_DP[t][0])
	# 남는 시간이 있는 경우 
	else : 
		print(chicken_DP[t][0], chicken_DP[t][1])
# 입력
a, b, t = [int(x) for x in input().split()]
# 출력 
solve(a, b, t)