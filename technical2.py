 
# Question 2
# Given a string a, find the longest palindromic substring contained in a. 
# Your function definition should look like question2(a), and return a string.

def question2(string):

    length  = 1
    start = 0
    low = 0
    high = 0

    s_len = len(string)

    for x in xrange(1, s_len):
        # First loop. Compare letters adjacent
        low = x - 1
        high = x
        while (low >= 0) and (high < s_len) and (string[low] == string[high]):
            # Letters match. Set start equal to low
            start = low
            # Set length equal to high + low and add 1 to offset index of 0
            length = high - low + 1
            low -= 1
            high +=1

        #Second Loop. Compare letters with 2 between them.
        low = x - 1
        high = x + 1
        while (low >= 0) and (high < s_len) and (string[low] == string[high]):
            # Letters match. Set start equal to low.
            start = low
            # Set length equal to high + low and add 1 to offset index of 0
            length = high - low + 1
            low -= 1
            high += 1
    if length > 1:
        return string[start:start + length]

    return None

    
def testQ2():
    print "Q2 Test1: expected outcome aba"
    print "Outcome : " + str(question2("aba"))
    print "Q2 Test2: expected outcome ll"
    print "Outcome : " + str(question2("hello"))
    print "Q2 Test3: expected outcome None"
    print "Outcome : " + str(question2("washington"))


testQ2()
