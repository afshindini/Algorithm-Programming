def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 1
    longest_length = 1
    current_length = 1
    
    n = len(A)
    for i in range(1,n):
        if A[i-1] < A[i]:
            current_length += 1
        else:
            current_length = 1
        
        if current_length > longest_length:
                longest_length = current_length
                count = 1
        elif current_length == longest_length:
                count += 1
    return count
