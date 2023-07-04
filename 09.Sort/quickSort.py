def quickSort(A, p:int, r:int):
	if p < r:
		 q = partition(A, p, r)   # 기준 원소 기준으로 분할, q = 분할 후 기준 원소 인덱스
		 quickSort(A, p, q-1)	 # 앞 부분 재귀
		 quickSort(A, q+1, r)	 # 뒷 부분 재귀

def partition(A, p:int, r:int) -> int:   
	# 1구역: 기준 원소보다 작다고 분류된 원소들 
	# 2구역: 기준 원소보다 크다고 분류된 원소들
	# 3구역: 아직 분류되지 않은 원소들
	# 4구역: 기준 원소 자신
	x = A[r]   # 기준 원소
	i = p-1   # i: 1구역의 끝 지점
	for j in range(p, r):   # j: 3구역의 시작 지점 (i < 2구역 < j)
		if A[j] < x:
			i += 1   
			A[i], A[j] = A[j], A[i]  
	A[i+1], A[r] = A[r], A[i+1]   # 기준 원소와 2구역 첫 원소 교환
	return i+1

# θ(nlogn)의 점근적 수행 시간을 가짐 (고급 정렬)
# 고급 정렬은 퀵, 병합, 힙 순으로 빠름
# 실전에서 매우 빨라 가장 선호
# 단점: 동일한 원소가 많이 존재하거나 리스트가 거의 정렬되어 있을 경우 θ(n^2)의 점근적 수행 시간을 가짐 
