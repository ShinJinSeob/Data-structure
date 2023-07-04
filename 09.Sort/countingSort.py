def countingSort(A):
	k = max(A)   # 최댓값
	C = [0 for _ in range(k+1)]   # 빈도리스트
	for j in range(len(A)):
		C[A[j]] += 1
	for i in range(1, k+1):
		C[i] = C[i] + C[i-1]   # 누적리스트
	B = [0 for _ in range(len(A))]    #정렬리스트
	for j in range(len(A)-1, -1, -1):
		B[C[A[j]]-1] = A[j]
		C[A[j]] -= 1   # 누적리스트 고침
	return B

# 정렬하고자 하는 원소의 값이 -O(n)~O(n) 범위의 정수인 경우 사용
# θ(n) 의 점근적 수행 시간을 가능 (두 원소 간의 비교를 하지 않고, 자신의 값으로 분류함으로써 가능)
