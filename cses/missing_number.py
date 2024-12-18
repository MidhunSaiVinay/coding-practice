def find_missing_number(arr, n):
    
    total_sum = n * (n + 1) // 2  # Sum of first n natural numbers
    actual_sum = sum(arr)  # Sum of array elements
    return total_sum - actual_sum

# Driver code
if __name__ == "__main__":
    # Missing number finder
    n = int(input())  # Input the size of the sequence
    arr = list(map(int, input().split()))  # Input the array elements
    missing_number = find_missing_number(arr, n)
    print(missing_number)