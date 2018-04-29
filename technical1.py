# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(txt, pat):
    list_str = list(txt)
    list_str.sort()
    p = len(pat)

    low = 0 # the start of the range of characters we are examining.
    high = len(list_str) - 1 # the ending range of characters we are examining
    j = 0 # represents 1 less than the minimum length needed for an anagram

    for i in xrange(0, p):
        while (low <= high): # We only continue if low position is less or equal to high position.
            mid = (low + high) / 2 # Calculate the middle value between low and high
            s_chr = list_str[mid]  # Middle string chr to compare. 
            p_chr = pat[i] # String character of the pattern to compare.
            if s_chr == p_chr and high-low > j: # If the two characters match
                # only count it as a match if the length between high and low is greater than
                # the number of characters already matched.  In other words, the match can only be
                # considered if it is of greater length than the already found matched string.
                j += 1 # we have a match.  Increment by anagram length by 1
                low = 0 # Set low to 0
                high = len(list_str) - 1 # Lower the high range by 1
                break
            elif (s_chr < p_chr): # If string character is of lesser value than pattern, we need to increment low
                low = mid + 1 # Set the low to the next character which is mid + 1
            else: # String character is greater value than pattern character, thus set high to middle -1
                high = mid - 1 
    if j == p: 
        return True # We have a match because the # of characters matched equals pattern length.
    return False


def testQ1():
    print "Q1 Test1: expected outcome False"
    print "Outcome : " + str(question1("udacity", "ud"))
    print "Q1 Test2: expected outcome True"
    print "Outcome : " + str(question1("udacity", "ac"))
    print "Q1 Test3: expected outcome False"
    print "Outcome : " + str(question1("udacity", "dc"))


testQ1()