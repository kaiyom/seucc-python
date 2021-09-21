  1 
  2 def numberToDigit(n):
  3     digits = []
  4     for k in str(n):
  5         digits.append( int(k))
  6     return digits
  7 
  8 def isArmStrong(n):
  9     digits = numberToDigit(n)
 10     result = 0
 11 
 12     for k in digits:
 13         result += k ** 3
 14 
 15     return result == n
 16 
 17 if __name__ == "__main__":
 18 
 19     try:
 20         n = int(input("Enter a number: "))
 21 
 22         if isArmStrong(n):
 23             print(f"{n} is a armstrong number")
 24         else:
 25             print(f"{n} is not a armstrong number")
 26 
 27     except Exception as ex:
 28         print(f"you got an error '{type(ex).__name__}'.")
 29 
