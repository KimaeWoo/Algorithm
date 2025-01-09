import heapq
import sys

input = sys.stdin.readline

MAX_Heap = []
result = []

N = int(input())
for i in range(N):
    x = int(input())
    if x == 0:
        if MAX_Heap:
            # heapq는 최소 힙이기 때문에 -를 붙여서 다시 양수로 뽑아낸다.
            result.append(-heapq.heappop(MAX_Heap))
        else:
            result.append(0)
    else:
        # heapq는 최소 힙이기 때문에 -를 붙여서 음수로 삽입한다.
        # -를 붙이면 가장 작은 수가 곧 가장 큰 수를 의미한다.
        heapq.heappush(MAX_Heap, -x)

for i in result:
    print(i)