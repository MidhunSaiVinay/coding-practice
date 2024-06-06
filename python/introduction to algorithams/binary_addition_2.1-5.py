def binary_addition(bin1, bin2):
    # Reverse the binary lists to start adding from the least significant bit
    bin1.reverse()
    bin2.reverse()

    # Initialize variables
    carry = 0
    sum_list = []

    # Iterate through the lists 
    for i in range(max(len(bin1), len(bin2))):
        # Get the bits from the lists or use 0 if the list is shorter
        bit1 = bin1[i] if i < len(bin1) else 0
        bit2 = bin2[i] if i < len(bin2) else 0

        # Perform binary addition
        total = bit1 + bit2 + carry

        # Calculate carry and update sum_list
        sum_list.append(total % 2)
        carry = total // 2

    # If there's still a carry after iterating through all bits
    if carry:
        sum_list.append(carry)

    # Reverse the sum_list to get the correct binary representation
    sum_list.reverse()

    return sum_list

# Example usage
bin1 = [1, 1, 0, 1]
bin2 = [1, 0, 1, 1]
result = binary_addition(bin1, bin2)
print(f"The sum of {bin1} and {bin2} is {result}")
