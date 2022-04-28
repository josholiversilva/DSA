# knuth-morris-pratt algorithm
# checks characters from left to right
# uses mismatch occurrences to determine where next match could begin
# bypassing re-examination of previously matched chars
# http://www.btechsmartclass.com/data_structures/knuth-morris-pratt-algorithm.html
#
# time: worst - O(MN)
#       best - O(M+N) where M=pattern table, N=search string


# naive
# check first, shift if no match & start form start pattern(backtrack)
# otherwise check next pattern char until match whole
def kmp_naive(input, pattern):
    curr = 0
    currInput, currPattern = 0, 0
    while curr != len(input)-1:
        if len(pattern) == currPattern:
            return "Found Pattern!"
        if input[currInput] == pattern[currPattern]:
            currInput += 1
            currPattern += 1
        else:
            curr += 1
            currInput = curr
            currPattern = 0
            print('-- mismatch --')
        
        print(input[currInput-1], pattern[currPattern-1])

# improved
# get prefix & suffix of unique chars
# avoid comparisons by storing prefix==suffix subpatterns
# & trace to avoid backtracking on string
# only the pattern's pointer will move

# prefix tables
# abcdabeabf    abcdeabfabc     aabcadaabe      aaaabaacd
# 0000120120    00000120123     0100101230      012301200

# 
# 0000120

import time
def kmp_optimized(input, pattern):
	p = create_prefix_table(pattern) # 00120

	# i: input ptr   -> ababcabcabaabababd
	# j: pattern ptr -> ababd
   	i,j = 0,0

	while i < len(input):
		if j == len(pattern):
			print(input, i, pattern, j)
			return True

		time.sleep(1)
		print(input[i], pattern[j]) 

		if input[i] == pattern[j]:
			i += 1
			j += 1
			continue
		
		while j > 0:
			# we get the previous prefix table of j
			# b/c we're finding valid prefix
			# before the mismatch (which is current j)
			j = p[j-1]
			time.sleep(2)
			print('inside inner while')
			print('new j: ' + str(j))
			print(input[i], pattern[j])

			if j == 0:
				print('j == 0, increase i')
				i += 1
				break

			if input[i] == pattern[j]:
				print(input[i] + ' == ' + pattern[j])
				i += 1
				j += 1
				break
		
	if j == len(pattern):
		print(input, i, pattern, j)
		return True
   	return False

def create_prefix_table(pattern):    
	# 1234567
	# abababaa	-> pattern
	# 00123451	-> p

	# abcdabd
	# 0000120
    p = [0]*len(pattern)
	i,j = 0,1
    for _ in range(len(pattern)-1):
		if (pattern[i] == pattern[j]):
			i += 1
		else:
			i = 0
			if (pattern[i] == pattern[j]):
				i += 1

		p[j] = i
		j += 1
		continue

	return p

x = 'ababcabcababbabdababdbd'
y = 'ababd'
#print('============== kmp naive ===============')
#print(kmp_naive(x,y))

print('')
print("Comparing input '{}' with pattern '{}'".format(x,y))
print('============== kmp optimized ===============')
print(kmp_optimized(x,y))

    	# abababaa
    	# 00123451

	# abcdabd	ababd
	# 0000120	00120

	# abcdabeabf    abcdeabfabc     aabcadaabe      aaaabaacd
	# 0000120120    00000120123     0100101230      012301200

#print('============== creating prefix table===============')
#print(create_prefix_table('abcdabd'))
#print(create_prefix_table('abababaa') == [0,0,1,2,3,4,5,1])
#print(create_prefix_table('abcdabd') == [0,0,0,0,1,2,0])
#print(create_prefix_table('abcdabeabf') == [0,0,0,0,1,2,0,1,2,0])
#print(create_prefix_table('abcdeabfabc') == [0,0,0,0,0,1,2,0,1,2,3])
#print(create_prefix_table('aabcadaabe') == [0,1,0,0,1,0,1,2,3,0])
