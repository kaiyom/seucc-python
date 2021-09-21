
def numberToDigit(n):
    digits = []
    for k in str(n):
        digits.append( int(k))
    return digits

def isArmStrong(n):
    digits = numberToDigit(n)
    result = 0
    
    for k in digits:
        result += k ** 3
    
    return result == n

if __name__ == "__main__":
    n = int(input("Enter a number: "))
    
    if isArmStrong(n):
        print(f"{n} is a armstrong number")
    else:
        print(f"{n} is not a armstrong number")

