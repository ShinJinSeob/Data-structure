import math

def radixSort(A):
	maxValue = max(A)   # 최댓값
	numDigits = math.ceil(math.log10(maxValue))   # 자릿수 계산
	bucket = [[] for _ in range(10)]   # 0, 1, ..., 9에 대한 10개의 리스트
	for i in range(numDigits):   # 낮은 자리수부터 정렬
		for x in A:
			y = (x // 10**i) % 10
			bucket[y].append(x)
		A.clear()
		for j in range(10):
			A.extend(bucket[j])
			bucket[j].clear()

# 정렬하고자 하는 원소들이 상수 k개 이하의 자릿수를 가진 자연수, 제한된 길이를 가진 알파벳으로 이루어진 특수한 경우 사용
# θ(n) 의 점근적 수행 시간을 가짐 (두 원소 간의 비교를 하지 않고, 자신의 값으로 분류함으로써 가능)
