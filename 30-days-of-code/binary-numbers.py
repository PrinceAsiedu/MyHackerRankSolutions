
def max_consecutive(number):
    # function for finding max consecutive 1's
    # the binary form of a base 10 number
    
    current_consecutive_1s = 0
    max_consecutive_1s = 0 

    while number > 0:
        if number % 2 == 1:
            current_consecutive_1s += 1
        else:
            current_consecutive_1s = 0
        if current_consecutive_1s > max_consecutive_1s:
            max_consecutive_1s = current_consecutive_1s
        number = number // 2
    return max_consecutive_1s

if __name__ == '__main__':
    # Test against first 100 whole numbers 
    for i in range(1,100 + 1):
        c_num = max_consecutive(i)
        print(f'number: {i} has {c_num} consecutive 1s', end='\n')
