# Given input of pins (n)
# where pin 1 = vi points
# 	pin 1,i+1 = vi*vi+1 points
#	vi = -inf < v < inf & vi = integer
# Determine max possible score

# exponential time algorithm
# 3 choices for each element of n repeated n times
# time = O(3^n)
count = []
def bowling_exp(n):
	if len(n) == 0:
		return 0
	if len(n) == 1:
		return n[0]
	
	count.append(1)
	return max(bowling_exp(n[1:]), bowling_exp(n[1:])+n[0], bowling_exp(n[2:])+n[0]*n[1])

# linear time algorithm
# memoization decreases time to linear after storing the max value
# of the current n length
# time = O(N)
memo = {}
count = []
def dp(n, curr=0):
    if len(n) == 0:
        return 0
    if len(n) == 1:
        return n[0]
    if memo.get(len(n)):
        return memo[len(n)]
    
    count.append(1)
    memo[len(n)] = max(dp(n[1:]), dp(n[1:])+n[0], dp(n[2:])+n[0]*n[1])
    return max(dp(n[1:]), dp(n[1:])+n[0], dp(n[2:])+n[0]*n[1])

n = [-3, 1, 1, 9, 1, 9, 2, -5, -5]
# max possible is
# (-5*-5)+(9*2)+(9*1)+1+1 = 25+18+9+1+2 = 55
#print(bowling_exp(n))
#print("num of instructions: {}".format(len(count)))

print(dp(n))
print("num of instructions: {}".format(len(count)))
