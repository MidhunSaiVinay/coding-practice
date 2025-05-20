def longest_repetition(dna):
    """Finds the length of the longest repetition in a DNA sequence."""
    max_length = 1
    current_length = 1

    for i in range(1, len(dna)):
        if dna[i] == dna[i - 1]:
            current_length += 1
            max_length = max(max_length, current_length)
        else:
            current_length = 1

    return max_length

# Driver code
if __name__ == "__main__":
    # DNA sequence longest repetition
    dna = input().strip()  # Input the DNA sequence
    result = longest_repetition(dna)
    print(result)
