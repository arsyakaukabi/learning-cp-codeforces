# Read the number of test cases
for _ in range(int(input())):
    # Read the length of the string
    n = int(input())
    
    # Read the input string and append a "0" at the end for easier processing
    original_string = input() + "0"
    
    # Initialize an empty string to store the result
    result_string = ""
    
    # Initialize two pointers, l and r, to keep track of the current position in the string
    left_pointer = 0
    right_pointer = 1
    
    # Loop until the right pointer reaches the end of the string
    while right_pointer < n:
        # If the character at the left pointer is equal to the character at the right pointer
        if original_string[left_pointer] == original_string[right_pointer]:
            # Add the character at the right pointer to the result string
            result_string += original_string[right_pointer]
            
            # Move the left pointer to the position after the right pointer
            left_pointer = right_pointer + 1
            
            # Move the right pointer to the position two steps ahead
            right_pointer += 2
        else:
            # If the characters are not equal, move the right pointer one step ahead
            right_pointer += 1
    
    # Print the result string
    print(result_string)
