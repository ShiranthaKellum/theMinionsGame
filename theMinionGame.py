
def isVowel (l):
    if l == "A" or l == "E" or l == "I" or l == "O" or l == "U":
        return True

    else:
        return False

def findTheWinner (w):
    sMarks = 0
    kMarks = 0
    length = len (w)

    for i in range (length):
        if isVowel (w[i]) == False:
            for j in range (1, length+1):
                s = w [i : i + j]                       # create substrings index i to i+j-1 length of j-1
                if (len (s) == j):
                    sMarks += 1
                    # print (s)
    
        
        else:
            for j in range (1, length+1):
                s = w [i : i + j]
                if (len (s) == j):
                    kMarks += 1
                    # print (s)

    # print (sMarks)
    # print (kMarks)
    if sMarks > kMarks:
        print ("Stuart", sMarks)

    elif kMarks > sMarks:
        print ("Kevin ", kMarks)

    else:
        print ("Draw")

if __name__ == '__main__':
    # word = "BANANA"
    word = input ()
    findTheWinner (word)