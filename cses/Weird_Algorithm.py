def weirdAlgo(n):
    output = [n]  # Include the initial value in the sequence
    while n != 1:  # The sequence ends when n equals 1
        if n % 2 == 1:
            n = (n * 3) + 1
        else:
            n = n // 2
        output.append(n)
    return output

# Driver code
if __name__ == "__main__":
    n = int(input())
    result = weirdAlgo(n)
    print(" ".join(map(str, result)))