#ques1

value1 = int(input("enter first number"))
value2 = int(input("enter second number"))
value3 = value1 + value2
print("the sum of the two numbers is:", value3)





#ques2
value4 = int (input ("enter a number"))

if (value4 % 2) == 0:

              print("even number")

else :

              print("odd number")






#ques3
import math

value5 = int(input("enter a number"))
factorial = math.factorial(value5)

print("The factorial of", value5, "is", factorial)







#ques4
str1= input("enter your name")
print("good morning {} , how are you?" .format(str1))




#ques5
samplefile = open('C:/Users/hp/OneDrive/Desktop/pyintern/demosrish.txt', 'w')
print(7,8,9 , file=samplefile)



#ques6
samplefile = open('C:/Users/hp/OneDrive/Desktop/pyintern/demosrish.txt', 'r')
filecontent = samplefile.read
print("content of file:", filecontent)




#ques7
str2 = input("enter a word")
print("the length of the word is", len(str2))




#ques8
str22 = "Hello"
str3 = " Welcome!!"
str4 = str22 + str3
print(str4)








#ques9
str33 = "python is fun"

if "python" in str33:
    print("Yes! it is present in the string")
else:
    print("No! it is not present")







#ques10
str44 = "mountains are epitome of beauty "
cap_str44 = str44.upper()
print(cap_str44)





#ques11 couldn't be executed.





#ques12
num = input("Enter Number: ")
sum = 0

for i in num:
    sum = sum + int(i)

print(sum)







#ques13
str5 = int(input("enter your birthyear"))
str6 =  2024 - str5
print("your age is : ", str6)







#ques14 couldn't be solved.


#ques15 couldn't be solved.


#ques16
from collections import Counter
str7 = "srishti"
frequency = Counter(str7)

print("Count of all characters is : " , str(frequency))








#ques17
str8 = input("enter a word")
new_word = str8[0].upper() + str8[1:]

print("The word after uppercasing initial character : " , new_word)









#ques18
str9 = "python"
str10 = "golang"

str9 = str9.lower()
str10 = str10.lower()

if(len(str9) == len(str10)):


    sorted_str9 = sorted(str9)
    sorted_str10 = sorted(str10)


    if(sorted_str9 == sorted_str10):
        print(str9 + " and " + str10 + " are anagram.")
    else:
        print(str9 + " and " + str10 + " are not anagram.")

else:
    print(str9 + " and " + str10 + " are not anagram.")








#ques19
punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''

str11 = "good evening!!!, he said goodbye and went."

no_punct = ""
for char in str11:
   if char not in punctuations:
       no_punct = no_punct + char

print(no_punct)






#ques20
total = 0
start = 0

list1 = [11, 6, 17, 38, 53]

while (start < len(list1)):
    total = total + list1[start]
    start += 1

print("Sum of all elements in given list: ", total)







#ques21
list2 = ["hello", 55, 67, "hello", 78]
print("original list is:",list2)
print("the count of occurance of 'hello': ", list2.count("hello"))








#ques22
list3 = [3,52,36,99]
x = min(list3)
y = max(list3)
print("the smallest element is",x)
print("the largest element is",y)









#ques23
celsius = int(input("enter temperature in celsius"))

fahrenheit = (celsius * 1.8) + 32

print("the temperature in fahrenheit is :" , fahrenheit)







#ques24
n1 = int(input("Enter First Number: "))
n2 = int(input("Enter Second Number: "))

print("{} + {} = ".format(n1,n2))
print(n1 + n2)

print("{} - {} = ".format(n1, n2))
print(n1 - n2)

print("{} * {} = ".format(n1, n2))
print(n1 * n2)

print("{} / {} = ".format(n1, n2))
print(n1 / n2)



#ques25 couldn't be solved.




#ques26
str = "python is fun"

print(str.startswith("python"))

print(str.endswith("boring"))










#ques27
str13 = "hello everyone!!"
New_list = list(str13)
print("the newly formed list is :", New_list)



#the end.
