# 원소 1~10 따라서 무조건 원소의 갯수는 15개 이하 
# Two Pointer
# 전처리 투포인터

# 입력
m, n = tuple(map(int, input().split()))
mat = [list(map(int, input().split())) for _ in range(m)]

row_mat = [[0 for _ in range(n)] for _ in range(m)]
col_mat = [[0 for _ in range(n)] for _ in range(m)]

for i in range(m):
	for j in range(n):
		if j == 0 :
			row_mat[i][j] = mat[i][j]
		else : 
			row_mat[i][j] = row_mat[i][j-1]+mat[i][j]

for i in range(n):
	for j in range(m):
		if j == 0 :
			col_mat[j][i] = mat[j][i]
		else : 
			col_mat[j][i] = col_mat[j-1][i]+mat[j][i]

def sub(mat, k, s, limit):
	if s == 0:
		ans = col_mat[s+limit][k]
	elif s >= 1: 
		ans = col_mat[s+limit][k] - col_mat[s-1][k]
	return ans

def num_submat(s, m, n, mat):
	count = 0 
	for i in range(m-s):
		k = 0 
		sum_sub = sub(mat, k, s, i)
		for j in range(n):
			while k < n-1 and sum_sub < 15:
				k += 1
				sum_sub += sub(mat, k, s, i)
			if sum_sub == 15 : 
				count += 1
			sum_sub -= sub(mat, j, s, i)
	return count

def sum_submat(m, n, mat):
	count = 0 
	for i in range(m):
		count += num_submat(i, m, n, mat)
	return count

# 출력
print(sum_submat(m, n, mat))