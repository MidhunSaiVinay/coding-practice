def hIndex(citations):
    citations.sort(reverse=True)
    h = 0
    for i, c in enumerate(citations):
        if c >= i + 1:
            h = i + 1
        else:
            break
    return h

# Example usage:
citations1 = [3, 0, 6, 1, 5]
print(hIndex(citations1))  # Output: 3

citations2 = [1, 3, 1]
print(hIndex(citations2))  # Output: 1