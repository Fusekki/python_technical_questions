# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

# Definition of anagram  : a word or phrase made by transposing the letters of another word or phrase.
# The word "secure" is an anagram of "rescue."
        
def question1(txt, pat):

    if txt is None or pat is None or len(pat) > len(txt):
        return False
    
    list_str = list(txt)

    list_str.sort()
    p = len(pat)

    low = 0 # the start of the range of characters we are examining.
    high = len(list_str) - 1 # the ending range of characters we are examining
    j = 0

    for i in xrange(0, p):
        while (low <= high): # We only continue if low position is less or equal to high position.
            mid = (low + high) / 2 # Calculate the middle value between low and high
            s_chr = list_str[mid]  # Middle string chr to compare. 
            p_chr = pat[i] # String character of the pattern to compare.
            # if s_chr == p_chr and high + low >= j:
            if s_chr == p_chr:
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

    print "Q1 Test1 (Edge case) null input: expected outcome False"
    print "Outcome : " + str(question1("udacity", None))

    print "Q1 Test2 (Edge case) pattern length greater than string length: expected outcome False"
    print "Outcome : " + str(question1("udacity", "Udacityz"))

    
    print "Q1 Test3 (Edge case) text string is null: expected outcome False"
    print "Outcome : " + str(question1(None, "ab"))


    print "Q1 Test4: expected outcome True"
    print "Outcome : " + str(question1("udacity", "uy"))
    print "Q1 Test5: expected outcome True"
    print "Outcome : " + str(question1("udacity", "ac"))
    print "Q1 Test6: expected outcome False"
    print "Outcome : " + str(question1("udacity", "dz"))



testQ1()