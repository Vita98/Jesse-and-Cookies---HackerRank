#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

import heapq

def cookies(k, A):
    # Write your code here
    heap = A
    heapq.heapify(heap)
    iteration = 0
    
    if len(A) == 1 and A[0] < k:
        return -1
    
    while heap[0] < k:
        if len(heap) == 1:
            return -1
        
        minV = heapq.heappop(heap)
        minVS = heapq.heappop(heap)
        
        newValue = minV + (2*minVS)
        heapq.heappush(heap, newValue)
        iteration += 1
        
    return iteration

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()