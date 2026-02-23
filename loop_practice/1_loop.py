# 
# Calculate the sum of numbers from 1 to N.
# Example Input: N = 5
Total=0
n=5
for i in range(1,n+1):
    Total=Total+i
print(Total)

        
s1="python is fun"
count=0
vowel="aeiou"
for i in s1:
    if i in vowel:
        count=count+1
print(count)
# learning is int and string can't add understand the function.



# Print numbers from 1 to 50 divisible by both 4 and 6.
num=[]
for i in range(1,50):
    if i%4==0 and i%6==0:
        num.append(i)
print(num)
# learning is we can't add integer in list for adding something in list use append function
