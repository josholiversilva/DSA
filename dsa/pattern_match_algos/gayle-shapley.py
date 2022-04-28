# gayle-shapley 
# monogomous pairs in a given group - stable pairing
# 1. All individuals have ranked members of opposite set
# 2. One of 2 chosen to make proposals
# 3. Proposing group will propose most preferable option until accepted
# 4. Being proposed 
#       - accept if first offer
#       - reject if worse than current offer
#       - accept if better than current offer. jilt previous offer
import random

males = ['a','b','c','d','e']
females = ['l','m','n','o','p']

malePrefer = {}
for male in males:
    random.shuffle(females)
    femaleTransform = {}
    for femaleIndex in range(len(females)):
        femaleTransform[femaleIndex+1] = females[femaleIndex]

    femaleTransform['curr'] = 1
    malePrefer[male] = femaleTransform

femalePrefer = {}
for female in females:
    random.shuffle(males)
    maleTransform = {}
    for maleIndex in range(len(males)):
        maleTransform[maleIndex+1] = males[maleIndex]

    maleTransform['curr'] = 1
    femalePrefer[female] = maleTransform

print("Male Preferences: {}".format(malePrefer))
print("Female Preferences: {}".format(femalePrefer))

def gayle_shapley(proposers, proposerPrefs, acceptors, acceptorPrefs):
    openProposers = set(proposers)
    openAcceptors = set(acceptors)
    
    #while openProposers:
    for proposer in openProposers:
        prefNum = proposerPrefs[proposer]['curr']
        currPref = proposerPrefs[proposer].get(prefNum)
        print(prefNum, currPref)
        if currPref in openAcceptors:
            print("{} likes {}".format(proposer,currPref))

        break

gayle_shapley(males, malePrefer, females, femalePrefer)