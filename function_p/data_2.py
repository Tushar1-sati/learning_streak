
# Write a function that takes a number n and prints whether it is Even or Odd.

def number (n):
    if n%2==0:
     return 'even'
    else:
       return 'odd'

a=number(4)
print(a)
b=number(7)
print(b)

# Sum of First N Natural Numbers
def sum_natural_num (n):
   total=0
   for i in range(1,n+1):
      total=total+i
   return total
   
x=sum_natural_num(5)
print(x)

    

#    Write a function that checks whether a number is Prime or not.

def prime_num(n):
    if n <= 1:
        return "Not Prime"

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Not Prime"
    return "Prime"
print(prime_num(10))


      

