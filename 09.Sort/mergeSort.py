def mergeSort(A, p:int, r:int):   # (리스트, 첫 원소, 끝 원소)
	if p < r:
		q = (p+r) // 2
		mergeSort(A, p, q)   # 앞부분 재귀 
		mergeSort(A, q+1, r)   # 뒷부분 재귀
		merge(A, p, q, r)   # 각 부분 병합 (수행되는 과정에서 정렬)

def merge(A, p:int, q:int, r:int):   
	i = p; j = q+1; t = 0   # (앞 부분 시작 레퍼런스, 뒷 부분 시작 레퍼런스, 정렬 리스트 인덱스)
	tmp = [0 for i in range(len(A))]   # 보조 리스트
	while i <= q and j <= r:   # 병합
		if A[i] <= A[j]:
			tmp[t] = A[i]; t += 1; i += 1
		else:
			tmp[t] = A[j]; t += 1; j += 1
	while i <= q:   # 나머지 처리
		tmp[t] = A[i]; t += 1; i += 1
	while j <= r:   # 나머지 처리
		tmp[t] = A[j]; t += 1; j += 1
	i = p; t = 0
	while i <= r:   # A로 옮김
		A[i] = tmp[t]; t += 1; i += 1

# θ(nlogn)의 점근적 수행 시간을 가짐 (고급 정렬)
# 고급 정렬은 퀵, 병합, 힙 순으로 빠름
# 단점 (1.보조 리스트로 인한 공간 낭비, 2.A로 옮기는 과정에서의 시간 낭비)
