def recursive_func(n):
    n = n - 1
    if n >= 0:
        print(n)
        recursive_func(n)

def main():
    n = 5
    print(n)
    recursive_func(n)   

main()