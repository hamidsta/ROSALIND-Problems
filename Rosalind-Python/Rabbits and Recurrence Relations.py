def fibo(x, y):
    if x <= 2:
        return 1
    else:
        return fibo(x-1,y) + y * fibo(x-2,y)

    with open("C:/Users/abdel/PycharmProjects/pythonProject1/rosalind_fib.txt", 'r') as f:
        x, y = f.readline().strip().split(" ")
        print(fibo(int(x), int(y)))