#requesting for the user input
k = int(input("Enter Number of Terms:"))
#initialize the starting values 
n1, n2 = 0, 1
count = 0
print("Fibonacci sequence:")
while count < k:
                     print(n1)
                     k1= n1 + n2
                     n1 = n2
                     n2 = k1
                     count += 1
