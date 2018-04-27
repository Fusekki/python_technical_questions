# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring of s. 
# For example: if s = "udacity" and t = "ad", then the function returns True. 
# Your function definition should look like: question1(s, t) and return a boolean True or False.

def question1(txt, pat):
    list_str = list(txt)
    list_str.sort()
    p = len(pat)

    low = 0
    high = len(list_str) - 1
    j = 0

    for i in xrange(0, p):
        while (low <= high):
            mid = (low + high) / 2
            if (list_str[mid] == pat[i]):
                j += 1
                low = 0
                high = len(list_str) - 1
                break
            elif (list_str[mid]  < pat[i]):
                low = mid + 1
            else:           
                high = mid - 1
    if j == p:
        return True
    return False


def testQ1():
    print "Q1 Test1: expected outcome True"
    print "Outcome : " + str(question1("udacity", "ud"))
    print "Q1 Test2: expected outcome False"
    print "Outcome : " + str(question1("udacity", "yz"))
    print "Q1 Test3: expected outcome False"
    print "Outcome : " + str(question1("udacity", "cily"))


testQ1()