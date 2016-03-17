# https://www.hackerrank.com/challenges/the-minion-game
strIn = input()
vowels = ['A','E','I','O','U']
stuartScore = 0
kevinScore = 0
for i in range(len(strIn)):
    # len(strIn)-i : Gives the total count of possible substrings which can be directly added to the score
    if strIn[i] in vowels:
        kevinScore = kevinScore + len(strIn)-i
    else: 
        stuartScore = stuartScore + len(strIn)-i
if stuartScore > kevinScore:
    print("Stuart",stuartScore)
elif kevinScore > stuartScore:
    print("Kevin",kevinScore)
else:
    print("Draw")


            
            