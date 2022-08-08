def fib(n, k):
    if n <= 2:
        return 1
    else:
        return fib(n-1,k) + k * fib(n-2,k)

if __name__ == "__main__":
    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_fib.txt", 'r') as f:
        n, k = f.readline().strip().split(" ")
        print(fib(int(n), int(k)))