#vars
varInt = 20
varInt = 30
varStr = 'word'
varBool = False

#prints
print(varInt)
print("hello world")

#user inputs
varInput = input("Input: ")
print("Input was "+ varInput)

#type conversion
#calculate age
#float(), int(), bool(), str()
birth_year = input("Input your birth year: ")
age = 2023 - int(birth_year)
print(age)

#calculator
num1 = input("First number: ")
num2 = input ("Second number: ")
sum = float(num1)+float(num2)
print("Sum: "+ str(sum))

#string testing
str2 = 'python string testing'
print(str2.upper())
print(str2.find('y'))
print(str2.find('Y'))
print(str2.find('string'))
    #variables are immutable
print(str2.replace('python','for'))
print(str2)
print('python' in str2)

#operators
print(1/3)
print(1//3)
x=10
x += 3
print(x)

y = 30
print(y>10 and y<30)

#logic
if y < 30:
    print("It's less than 30")
elif y > 30:
    print("It's than 30")
else:
    print("None of the above")
print('Outside loop')

i=1
while i<=5:
    print(i)
    print(i * 'x')
    i+=1

#lists
list = ["Hello","My","Name","Is"]
print(list[0])
print(list[-2])
list[0] = "Hi"
print(list)
print(list[0:3])

list.append('Kate')
print(list)

list.insert(4,'Miss')
print(list)

list.remove('Hi')
print(list)

print('Name' in list)
print(len(list))

list.clear()
print(list)


#for loops
nums = [1,2,3,4,5]
for item in nums:
    print(item)

nums2=range(5,10,2) #start, stop(non-inclusive), step
print(nums2)
for num in nums2: #or for num in range(5,10,2)
    print(num)

#tuples, if you use parenthesis its immutable
nums3 = (1,2,3)