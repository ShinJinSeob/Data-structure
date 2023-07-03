def bubbleSort(A):
	for numElements in range(len(A), 0, -1):   # 끝 원소부터 역순으로 정렬
		for i in range(numElements-1):   # 앞 원소부터 일일이 비교
			if A[i] > A[i+1]:
				A[i], A[i+1] = A[i+1], A[i]

# n^2의 점근적 수행 시간을 가짐 (기본 정렬)
# 기본 정렬은 삽입, 선택, 버블 순으로 빠름
