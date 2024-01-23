def plusOne(digits):
        carry = 1
        result = []

        for digit in reversed(digits):
            current_sum = digit + carry
            result.append(current_sum % 10)
            carry = current_sum // 10

        while carry:
            result.append(carry % 10)
            carry //= 10

        return result[::-1]
if __name__ == "__main__":
    # Example 1
    input_digits1 = [3,6,5]
    output_digits1 = plusOne(input_digits1)
    print(f"Input: {input_digits1}")
    print(f"Output: {output_digits1}")
    print()
