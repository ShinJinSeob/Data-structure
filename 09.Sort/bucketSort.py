import math
from DS.sort.insertionSort import insertionSort

def bucketSort(A):   # [0, 1) 범위의 실수 정렬
	n = len(A)
	B = [[] for _ in range(n)]   # 버킷리스트
	for i in range(n):
		B[math.floor(n*A[i])].append(A[i])
	A.clear()
	for i in range(n):
		insertionSort(B[i])   # 각 버킷리스트에 대해 삽입정렬
		A.extend(B[i])

# 정렬하고자 하는 원소들이 균등 분포일 때 사용
# θ(n) 의 점근적 수행 시간을 가짐 (두 원소 간의 비교를 하지 않고, 자신의 값으로 분류함으로써 가능)
