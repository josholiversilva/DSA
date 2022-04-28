'''
def reverseString(inputString):
    outputString = ''
    for char in inputString:
        outputString = char + outputString

    return outputString

inputString = "hello world"
print(reverseString(inputString))

# find all pairs that equal a value k in arr
def pairEqualK(arr, k):
    ans = []
    track = set()
    for num in arr:
        pair = abs(num - k)
        if pair in track:
            ans.append((num,pair))
        track.add(num)

    return ans
    
arr = [6,4,2,0,1,5]
k = 6
print(pairEqualK(arr,k))

def fizzbuzz(n):
    ans = []
    for num in range(1,n+1):
        curr = []
        if num % 3 == 0:
            curr.append("fizz")
        if num % 5 == 0:
            curr.append("buzz")
        if not curr:
            curr.append(str(num))

        ans.append(''.join(curr))

    return ans

print(fizzbuzz(15))
'''
















# sys library
import sys

# function call
# define function -> our logic here, but thats it
def ship_list_func(ship1, ip, num):
    print(ship1, ip, num)


if __name__ == '__main__':
    ship1 = sys.argv[1]
    ip = sys.argv[2]
    num = sys.argv[3]

    # use the defined function called ship_list_func()
    # which is referencing line 67
    ship_list_func(ship1, ip, num)