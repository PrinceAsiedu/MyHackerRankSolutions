# Given an array, A, of N integers, print A's elements in reverse order 
# as a single line of space-separated numbers.

#Input Format
# The first line contains an integer, N(the size of our array).
# The second line contains N space-separated integers that describe array A's elements.

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))
    for i in range(1, n + 1):
        print(arr.pop(), end=' ')
        # print(*arr[::-1]) # Later learned this is another way of doing it.
