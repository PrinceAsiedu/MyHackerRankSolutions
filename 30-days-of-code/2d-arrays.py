def get_hourglass_sum(maxtrix, row, col):
    sum = 0
    sum += maxtrix[row-1][col-1]
    sum += maxtrix[row-1][col]
    sum += maxtrix[row-1][col+1]
    sum += maxtrix[row][col]
    sum += maxtrix[row+1][col-1]
    sum += maxtrix[row+1][col]
    sum += maxtrix[row+1][col+1]
    return sum


if __name__ == '__main__':

    arr = []
    max_hourglass_sum = -63
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    for i in range(1, 5):
        for j in range(1, 5):
            current_hourglass_sum = get_hourglass_sum(arr, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    print(max_hourglass_sum)
