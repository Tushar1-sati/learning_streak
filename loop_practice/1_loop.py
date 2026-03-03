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


#  Calculate the sum of all even numbers in a list.
# Input: [1, 4, 7, 10, 12]
l1=[1, 4, 7, 10, 12]
even=[]
for i in l1:
    if i%2==0:
        even.append(i)
    print(even)
print(sum(even))

# Print numbers between 1–50 divisible by 3 or 5
l1=[]
for i in range(1,51):
    if i%3==0 or i%5==0:
        l1.append(i)
print(l1)

# Find the largest number in a list.
# Input: [5, 12, 3, 21, 7]
l1=[5, 12, 3, 21, 7]
max_num=l1[0]
for i in l1:
    if i> max_num:
        max_num=i
print(max_num)
