from module5_mod import Numbers

def main():
    N = int(input("Enter a positive integer N: "))
    if N <= 0:
        print("N must be a positive integer.")
        return

    numbers = Numbers()

    print(f"Enter {N} numbers:")
    for i in range(N):
        num = int(input(f"Number {i + 1}: "))
        numbers.insert_number(num)

    X = int(input("Enter number X to search: "))
    result = numbers.search_number(X)
    print(result)

if __name__ == "__main__":
    main()
