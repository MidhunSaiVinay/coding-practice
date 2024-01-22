N=int(input())
def exactly3Divisors(self, N):
    def sieve(n):
        isprime = [True] * (n + 1)
        isprime[0] = isprime[1] = False
    
        for i in range(2, int(n**0.5) + 1):
            if isprime[i]:
                for j in range(i*i, n+1, i):
                    isprime[j] = False

        return [i for i in range(2, n+1) if isprime[i]]
    a=sieve(int(N**0.5))
        
    return len(a)