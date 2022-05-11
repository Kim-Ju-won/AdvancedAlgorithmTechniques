'''
알고리즘 설명: 이 알고리즘은 이진 탐색을 이용해서 횟수를 계산합니다. 이진탐색이 가능한 이유를 살펴보도록 하겠습니다. A리스트의 처음, 중간, 끝을 start, mid, last라고 가정합시다. 이 상황에서 왼쪽 rotation이 없는 경우에 서로다른 수가 오름차순으로 주어지므로 A[start] < A[mid] < A[last]가 됩니다. 하지만 왼쪽 rotation이 생길 경우에는 이러한 부등식이 성립하지 않습니다. 우선 mid보다 적은 숫자 만큼 왼쪽 rotation한 경우는 A[last] > A[mid]가 되고, mid보다 많은 숫자만큼 왼쪽 rotation을 하게되면 A[start] > A[mid]가 되게 됩니다. 그리고 각 상황에서 왼쪽 방향으로 rotation했을 때 제일 처음 이동한 원소는 전자의 경우에 mid~last사이에 그리고 후자의 경우에는 start ~ mid에 존재하게 됩니다. 따라서 이진탐색을 이용해서 각 케이스 마다 해당 구간에 이동하고 그 구간의 A[mid]가 양옆을 비교해봤을 때 오름차순이 아닌 왼쪽 rotation이 생길 경우 처음 이동한 원소의 인덱스가 됩니다. 그리고 이 인덱스와 전체 리스트 길이와의 차이를 통해 rotation수를 계산하고 반환하여 회전 횟수를 구할 수 있습니다. 

Big-O수행시간 : O(logn) 
이 함수는 이진 탐색 방식의 알고리즘으로 구현 되어 있습니다. 변수 선언, 예외처리는 각각 O(1) 상수시간에 해결할 수 있고 핵심적으로 봐야할 부분은 "왼쪽 방향 rotation을 했을 때 제일 처음 이동한 원소"를 찾아가는 탐색부분입니다. 
전체 binary_check_rotation함수를 T(n)으로 봤을 떄 재귀적으로 호출 하는 부분을 살펴보면, num[mid] > num[last]일 때와 num[start] > num[mid]일 때 해당하는 원소길이의 1/2구간을 부르게 됩니다. 따라서 이 부분은 T(n/2)가 됩니다. 그리고 경우에 따라 절반에 해당하는 구간은 한번 선택됩니다. 점화식으로 정리해보면 T(n) = T(n/2) + c (단,c는 상수)로 되고 이 점화식을 풀어보면 T(n) = T(n/2) + c = (T(n/4) + c) + c  = (T(n/8) + c) + c + c = ... = T(n/2^k) + c + ... + c  = ck + c = logn(c+1)이 되어 빅오시간은 logn이 됩니다.

'''
# 함수
def binary_check_rotation(num, start, last):
	# 왼쪽 rotation을 했을 때 제일 처음 이동한 원소의 index를 저장하는 변수
	index = 0
	mid = (start+last) //2
	# 왼쪽 rotation이 없는 경우(예외처리)
	if num[start] < num[mid] and num[mid] < num[last] :
		return index 
	
	# 이진탐색 수행시간 : T(n) = T(n/2) + C => T(n)
	# 왼쪽 rotation을 했을 때 제일 처음 이동한 원소의 index를 찾을 경우
	if num[mid-1] > num[mid] and num[mid] < num[mid] + 1:
		index = mid
		# 해당 인덱스를 길이에서 빼서 왼쪽 rotation수 반환
		return len(num)-index
	# 맨 끝 원소가 중간 원소보다 클경우 해당 구간 탐색
	elif num[mid] > num[last] : 
		return binary_check_rotation(num, mid, last) # T(n/2)
	# 맨 처음 원소가 중간 원소보다 작을 경우 해당 구간 탐색
	elif num[mid] < num[start] : 
		return binary_check_rotation(num, start, mid) # T(n/2)

# 입력
num = list(map(int, input().split()))
# 출력
print(binary_check_rotation(num, 0, len(num)-1))
'''
알고리즘 설명 : 이 두번째 알고리즘은 왼쪽 방향으로 1번 이상 rotation이동을 할 경우 A리스트안에서 A[i]>A[i+1]인 구간이 생기는 원리를 이용해서 알고리즘을 구현해주었습니다. 리스트 A의 처음부터 배열을 순서대로 스캔하며 배열의 A[i] > A[i+1]이 일어나는 구간의 인덱스를 check변수에 저장합니다. 해당 인덱스는 k번 왼쪽 rotation이 일어난 경우 가장 처음으로 오는 원소가 됩니다.따라서 A리스트의 길이에서 제일 처음 왼쪽 rotation이 일어난 인덱스를 빼주어 전체 왼쪽 rotation 횟수를 반환합니다. 또한 만약 왼쪽 rotation이 일어나지 않는 경우는 없는 경우는 0으로 설정해줍니다. 이 알고리즘 또한 제출하여 모든 테스트케이스를 통과 해주었습니다.
Big-O 수행시간 : O(n)
check_rotation 함수는 '변수선언 - for루프 - 값 반환' 형식으로 이루어져있습니다. 변수 선언은 O(1) 상수시간이 걸리고, 반환 할 때 비교연산자로 check=0인지 체크하는 부분 한 부분으로 O(1)이 됩니다. 유의깊게 봐야하는 부분은 O(n)부분인데, for루프문 안에서 단순히 A[i] > A[i+1]인지 상수시간 비교가 일어나므로 O(n)이 됩니다. 따라서 전체 알고리즘의 빅오시간은 O(n)이 됩니다. 

def check_rotation(num):
	# 왼쪽 rotation이 일어났을 첫 원소를 저장하는 index
	check = 0
	# O(n) : for 루프를 돌며 왼쪽 rotation이 일어났는지 체크 
	for i in range(1,len(num)-1):
		# 왼쪽 rotation이 일어났는지 체크
		if num[i] > num[i+1]:
			check = i+1
	
	# 왼쪽 rotation이 일어나지 않았으면 0을 리턴
	if check == 0 : 
		return 0
	# 왼쪽 rotation이 일어났으면 A리스트의 길이에서 check변수를 빼주어 왼쪽 rotation계산 후 반환
	return len(num)-check
	
# 입력 
num = list(map(int, input().split()))
# 출력 
print(check_rotation(num))
'''