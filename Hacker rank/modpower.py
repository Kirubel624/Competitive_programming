# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    m = int(input())

    result_1 = pow(a, b)
    result_2 = pow(a, b, m)

    print(result_1)
    print(result_2)