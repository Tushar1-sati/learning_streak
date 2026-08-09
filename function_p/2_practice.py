# Write fizzbuzz_range(n) that prints numbers 1 to n, but for multiples of 3 print "Fizz", multiples of 5 print "Buzz",
#  multiples of both print "FizzBuzz".

def fizzbuzz_range(n):
   """ fizzbuzz_range print num 1 to n"""
   for i in range(1,n+1):
      if i%3==0 and i%5==0:
         print('fizzbuzz')
      elif i%3==0:
       print ('fizz')
      elif i%5==0:
        print('buzz')
      else:
        print (i)

a=fizzbuzz_range(15)

# factorial of 5
def factorial (x):
  for i in range(1,x+1):
    if i*1==0:
      


    




            