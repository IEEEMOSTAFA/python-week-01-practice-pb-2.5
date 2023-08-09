
def digits_of_number(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    list= digits
    return list
    

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        digits = digits_of_number(n)
        for digit in digits:
            print(digit, end=" ")
        print()

if __name__ == "__main__":
    main()
        
