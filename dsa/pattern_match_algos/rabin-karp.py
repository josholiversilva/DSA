# rabin-karp
# Easier implementation assuming collision will never happen
# Great for small search strings, strong find hash patterns
#
# key words
# 1. rolling hash function: 
#       - static sliding window that continues hash function in list
# 2. hash function:
#       - h(p) where h=hash, p=pattern
# 3. key,vals:
#       - use ascii or own key:val i.e. a-1, b-2..
# 4. hash:
#       - resulting value from hash function


# avg time: O(mn) with "spurious hits"
# opt time: O(n-m+1) with NO "spurious hits" -> strong hash function

keyVals = {}
keys = ['a','b','c','d','e','f','g','h','i','j']
for keyIndex in range(len(keys)):
    keyVals[keys[keyIndex]] = keyIndex+1

def rabin_karp_direct_hash(txt, pattern):
    patternStart = []
    spuriousHits = 0
    patternVal = 0
    for charVal in pattern:
        patternVal += keyVals[charVal]

    hashLength = len(pattern)
    txtVal = 0
    tail = 0
    for curr in range(len(txt)):
        txtVal += keyVals[txt[curr]]
        if curr < hashLength-1:
            continue # avoids spurious hit

        #print(txtVal, patternVal)
        if txtVal != patternVal:
            txtVal -= keyVals[txt[tail]]
            tail += 1
            continue # avoids spurious hit
        
        #print('spurious hit')
        spuriousHits += 1
        # spurious hit -> leads to more time (worst case bad hash function)
        # change hash txtVal & patternVal with stronger hash function for less spurious hits
        # match vals, so verify same
        if isMatch(txt[tail:curr+1], pattern):
            patternStart.append(tail)
        
        txtVal -= keyVals[txt[tail]]
        tail += 1
        
    print("Number of spurious Hits: {}".format(spuriousHits))
    print("Len of txt: {}".format(len(txt)))
    return "Pattern found at {}".format(patternStart)

def rabin_karp_good_hash(txt, pattern):
    spuriousHits = 0
    hashLen = len(pattern)-1
    powerRef = len(keys)
    if hashLen > len(txt)-1:
        return False

    patternVal = initializeValOfLen(pattern, hashLen+1)
    txtVal = initializeValOfLen(txt, hashLen+1)

    tail = 0
    verified = False
    for txtIndex in range(hashLen, len(txt)):
        #print(txtVal, patternVal)
        if txtVal != patternVal:
            # 412 - (4*10**2) = 412-400 = 12
            txtVal -= keyVals[txt[tail]] * powerRef**hashLen
            if txtIndex+1 < len(txt):
                # 12*10+5= 125
                txtVal = txtVal*powerRef+keyVals[txt[txtIndex+1]]
                tail += 1
            continue 

        #print('spurious hit')
        spuriousHits += 1
        # spurious hit -> leads to more time (worst case bad hash function)
        # hash value strong ~1 hit so O(n-m+1)
        if isMatch(txt[tail:txtIndex+1], pattern):
            return True


    print("Number of spurious Hits: {}".format(spuriousHits))
    print("Len of txt: {}".format(len(txt)))
    return False

def initializeValOfLen(valType, valLen):
    val = 0
    for valIndex in range(valLen):
        val += keyVals[valType[valIndex]] * len(keys)**(valLen-valIndex-1)

    return val

def isMatch(txt, pattern):
    for hashIndex in range(len(pattern)):
        if txt[hashIndex] != pattern[hashIndex]:
            return False

    return True 
        
txt = "bddabdbadbadbadbadbadbadbadbdabdbadbdadbdabdbadbadbadbadbadbadbadbadbdabdbadbadbadbad"
pattern = "dab"
print('====================== direct hash ======================')
print(rabin_karp_direct_hash(txt, pattern))
print('bad hash -> O(n*m) where n=len of txt, m=len of pattern')
print('rolling hash = O(n)')
print('letter verification = O(m)')

print('====================== good hash ======================')
print(rabin_karp_good_hash(txt,pattern))
print('good hash -> O(n-m+1) with NO spurious hits')
