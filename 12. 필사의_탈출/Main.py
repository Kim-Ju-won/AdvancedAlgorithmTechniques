'''
알고리즘 설명 : 이 알고리즘은 세 벽을 직선으로 통과한다에 초점을 두어 고안한 알고리즘입니다. 가장 윗벽, 중간 벽, 가장 아랫벽은 각각 y축(위아래)로 1 차이가 납니다. 그리고 해당하는 세지점을 통과하는 직선이어야만 통과할 수 있습니다. 따라서 같은 기울기를 가져야하며, 중간 점의 좌표를 middle, 위의 좌표와 아래의 좌표를 upper, down 이라고 하면 middle = (upper+down)/2를 만족해야됩니다. 따라서 해당 식을 통해 중간 장벽의 후보군을 구해주고, 그 후보군이 실제로 존재하는지 체크해주는 과정을 통해 모든 경우의 수를 계산하는 알고리즘입니다.
Big-O 수행시간 : O(n^2)
이 알고리즘은 크게 두 파트로 나눌 수 있습니다. 첫 번째 파트는 중간 벽의 후보군을 구해주는 부분이고, 그리고 그 후보군이 실제 중간벽에 있는지 확인하는 부분입니다. 
중간 벽의 후보군을 구해주는 함수는 간단합니다. 이중 for루프문을 돌면서 middle = (upper+down)/2의 값을 check라는 딕셔너리에 추가해줍니다. 있는 경우에는 +1, 없는 경우에는 1로 초기화를 해주어, 해당 후보군을 통과할 수 있는 경우의 수를 저장해줍니다. 따라서 이중 딕셔너리 삽입연산에는 O(1)그리고 이중 루프문이므로 O(n^2)을 곱해줘서 총 O(n^2)이 걸립니다. 
이후 후보군이 있는지 체크해주는 부분입니다. 중간벽에 있는 구멍이 저장된 리스트를 순서대로 스캔하면서 check에 있는지 체크합니다. check에 있는지 확인할 때는 딕셔너리는 hash-table을 따르고 있으므로 평균적으로 O(1)을 보장합니다. 따라서 O(1)*n = O(n)이 됩니다. 
따라서 O(n^2)+O(n)= O(n^2)이므로 빅오 수행시간은 O(n^2)입니다.
'''
# 함수
def escape(first, second, third):
	# 중간 벽 후보군에 저장할 변수 
	check = dict()
	# O(n^2) ; 두개의 이중 for루프문을 돌고 있기에 O(n)입니다.
	# 이 이중루프문에서는 윗 벽과 아랫벽 중간지점의 값을 구하는 for루프문입니다. 해당 값을 딕셔너리에 저장합니다.
	for first_hole in first : 
		for third_hole in third : 
			candidate = (first_hole+third_hole)/2
			if candidate in check : 
				check[candidate] += 1
			else : 
				check[candidate] = 1
			
	# O(n) : O(n) * O(1) = O(n)입니다.
	count = 0
	# 순서대로 중간벽에 있는 구멍을 미리 구한 check 해시 테이블(딕셔너리)에 존재하는지 확인합니다.
	for second_hole in second:
		# check는 딕셔너리로 Hash Table구조를 택하고 있습니다. key를 통해서 중간 장벽의 원소를 확인하고 있으므로 평균적으로 O(1) 상수시간을 보장합니다. 
		if second_hole in check : 
			# 존재할 경우 헤딩 중간 벽 구멍을 통과할 수 있는 경우의 수를 더해줍니다.
			count += check[second_hole]
	return count

# 입력
number_of_first_wall = int(input())
first = list(map(int, input().split()))
number_of_second_wall = int(input())
second = list(map(int, input().split()))
number_of_third_wall = int(input())
third = list(map(int, input().split()))
# 결과 
print(escape(first, second, third))