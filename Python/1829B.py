t = int(input())  # Number of test cases

for _ in range(t):
    n = int(input())  # Length of the array
    arr = list(map(int, input().split()))  # Elements of the array

    max_blank_space = 0  # Length of the longest blank space
    current_blank_space = 0  # Length of the current consecutive segment of zeros

    for i in range(n):
        if arr[i] == 0:
            current_blank_space += 1
            max_blank_space = max(max_blank_space, current_blank_space)
        else:
            current_blank_space = 0

    print(max_blank_space)
