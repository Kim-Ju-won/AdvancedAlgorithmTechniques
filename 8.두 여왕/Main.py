'''
알고리즘 설명: 
알고리즘은 체스 보드를 스캔하며 여왕의 위치를 찾아주는 방식을 선택했습니다. 배열을 선언하여 직접 Q를 놓는 것 보다는 해당 위치에 대한 특성을 이용해서 모든 경우를 탐색하는 방식으로 코드를 구현하였습니다. 우선 Two_Queens함수를 이용하여 이중루프문으로 체스 보드에 Q이 놓이는 모든 경우를 체크합니다. 그리고 해당 위치에서 check_queen_place라는 함수를 호출하여 같은 행이나 열 대각선이 아닐때 해당 경우의 수를 누적으로 연산하여 두 번째 Q가 놓일 수 있는 경우의 수를 구해줍니다. 이 경우의 수를 구할 때도, 이중 루프문을 이용해서 첫 번째 Q가 정해졌을 때 두번째 Q의 위치를 체크합니다.
'''
'''
Big-O 수행시간 : O(n^4)
이 코드의 수행시간은 크게 두 함수의 수행시간 분석을 통해 쉽게 파악할 수 있습니다. 
우선 처음 호출 되는 함수인 Two_Queens는 이중루프문을 돌며 첫번째 Queen의 위치를 정해줍니다. 그리고 가장 안에 for문에서 두 번째로 올수 있는 Queen의 위치를 정해주기 위해서 check_queen_place를 호출합니다. 이 함수 역시 이중루프문을 n*n의 크기만큼 돌며 확인하고 있으므로 이 수행시간은 O(n^2)이 됩니다. 
따라서 최종적으로 Two_Queens코드는 O(n^2) * O(n^2) = O(n^4)됨을 알 수 있습니다.
'''
# Queen 갯수를 파악할 변수
def check_queen_place(i,j):
	# Queen이 올 수 있는 자리 체크
	check = 0
	# 이중 for문을 통해 위치 탐색
	for k in range(0,n):
		for l in range(0,n): 
			# 같은 행, 열, 대각선이 아닌 경우 Queen이 올 수 있으므로 해당 자리 체크
			if not(i == k or j == l or abs(i-k) == abs(j-l)) : 
				check += 1
	return check
	
def Two_Queens(n):
	# Queen이 올수 있는 경우의 수
	count = 0
	# 체스 보드를 완전 탐색하여 첫 번째로 올려놓을 Queen자리 체크
	for i in range(0, n):
		for j in range(0,n):
			# 첫번째 Queen의 위치가 정해졌을 때 두 번째 Queen의 위치의 경우의 수를 더해줌
			count += check_queen_place(i, j)
					
	return count//2 # 중복된 값 제거 

#입력 
count = 0
n = int(input())
#출력
print(Two_Queens(n))
