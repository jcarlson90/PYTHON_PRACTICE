MY_CONSTANT  = 5
# constants do not exist in python, convention is to name in all caps
my_variable = "Hello World"
# all variable by default are re-assignable, snake case is the norm in python

#print varibale to the console with the print function
print(MY_CONSTANT)
print(my_variable)

########## if statements ##########
num = 5

if (num > 3):
    print("num is greate than 3")
elif (num > 1):
    print("num is greater than 1")
else: 
    print("num is 1 or less")

# indentation is required in python
    
num = 10

if (num > 9):
    print("num is greater than 9")
elif (num < 20):
    print("num is less than 20")
else:
    print("num is 9 or less")

##

x = 3
y = 10

if x < y:
    print("y is greater than x")

##
    
counter = 0
while (counter < 10):
    print(counter)
    counter += 1

# Palindrome
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
        return stirng == reversedString
    

# Binary Search Tree
def binarySearch(arr, tar):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left+right) // 2
        if tar < arr[mid]:
            right = mid -1
        elif tar > arr[mid]:
            left = mid + 1
        elif arr[mid] == tar:
            return mid
        
    return -1








 
    





