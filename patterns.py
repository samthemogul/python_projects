n = int(input("Enter value of n: "))

# Draw top half and middle of the triangle
for leftStars in range(n) :
   for column in range(2 * n - 1) :
      firstStar = n - 1 - leftStars
      lastStar = n - 1 + leftStars
      if column < firstStar or column > lastStar :
         print("-", end="")
      else :
         print("*", end="")
         
   print()
   # Draw bottom half of the triangle
for rightStars in range(n-1,-1,-1):
   for column in range(2 * n - 1) :
      firstStar = n - 1 - rightStars
      lastStar = n - 1 + rightStars
      if column < firstStar or column > lastStar :
         print("-", end="")
      else :
         print("*", end="")
         
   print()