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

# Heaps Sort
def heapSort(arr):
    n = len(arr)
    def heapify(arr, N, i, m):
        mini = i
        li, ri = 2 * i - N, 2 * i - N - 1
        if li >= m and arr[mini] > arr[li]: mini = li
        if ri >= m and arr[mini] > arr[ri]: mini = ri

        if mini != i:
            arr[i], arr[mini] = arr[mini], arr[i]
            heapify(arr, N, mini, m)

    for i in range(n - n // 2, n):
        heapify(arr, n, i , 0)

    for i in range(n):
        arr[i], arr[n-1] = arr[n - 1], arr[i]
        heapify(arr, n, n - 1, i + 1)
    return arr

# Two Number Sum

def twoNumberSum(arr, tarSum):
    storage = set(num for num in arr)

    for num in arr:
        tar = tarSum - num
        if tar in storage and tar is not num:
            return [num, tar]

    return []








 
    





