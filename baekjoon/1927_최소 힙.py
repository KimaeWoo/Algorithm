import sys

def add(PQ, x):
    index = len(PQ)
    PQ.append(x)  # 새로운 값을 리스트 끝에 추가
    while index > 1:
        parent = index // 2  # 부모 노드의 인덱스
        if PQ[parent] > PQ[index]:  # 부모가 더 크면, 자식과 교환
            PQ[index], PQ[parent] = PQ[parent], PQ[index]
            index = parent  # 부모로 이동
        else:
            break  # 힙 조건 만족하면 종료

def sub(PQ):
    if len(PQ) <= 1:
        result.append(0)  # 우선순위 큐가 비어 있으면 0 추가
        return
    
    result.append(PQ[1])  # 루트값 추가
    
    # 마지막 요소를 루트로 이동
    k = PQ.pop()  # 마지막 요소 제거 및 반환
    if len(PQ) == 1:
        return  # 큐에 더 이상 자식이 없으면 종료

    PQ[1] = k  # 마지막 요소를 루트에 배치
    
    index = 1
    while index * 2 < len(PQ):  # 자식 노드가 있을 때까지 반복
        left = index * 2
        right = left + 1
        smallest = index

        # 왼쪽 자식과 오른쪽 자식 중 더 작은 값을 찾음
        if left < len(PQ) and PQ[left] < PQ[smallest]:
            smallest = left
        if right < len(PQ) and PQ[right] < PQ[smallest]:
            smallest = right

        if smallest != index:  # 힙 조건 위반 시 교환
            PQ[index], PQ[smallest] = PQ[smallest], PQ[index]
            index = smallest  # 교환 후 자식으로 이동
        else:
            break  # 힙 조건 만족하면 종료

# 우선순위 큐 초기화 (1번 인덱스를 사용하기 위해 빈 값을 넣어줌)
priorityQueue = [None]
result = []

# 입력 처리
input = sys.stdin.readline  # readline을 함수로 호출

N = int(input())  # 첫 번째 줄은 연산 횟수
for i in range(N):  # 나머지 줄은 연산 데이터
    x = int(input())
    if x == 0:
        sub(priorityQueue)
    else:
        add(priorityQueue, x)

# 결과 출력
sys.stdout.write("\n".join(map(str, result)) + "\n")

"""
# heapq를 활용한 우선순위 큐
import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

PQ = []
result = []

N = int(data[0])

for i in range(1,N+1):
    x = int(data[i])

    if x == 0:
        if PQ:
            result.append(heapq.heappop(PQ))
        else:
            result.append(0)
    else:
        heapq.heappush(PQ,x)

# 결과를 출력할 때 한 번에 출력
sys.stdout.write("\n".join(map(str, result)) + "\n")
"""
