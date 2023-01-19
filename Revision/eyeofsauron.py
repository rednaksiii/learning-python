# Input consists of a single string of length where 
# Input strings will consist only of three types of characters: 
# vertical bars, open parentheses, and closing parentheses. 
# Input strings contain one or more vertical bars followed
# by a set of matching parentheses (the “eye”), followed by 
# one or more vertical bars. For a drawing to be “correct”, 
# the number of vertical bars on either side of the “eye” must match. 
# Input will always contain a pair of correctly matched parentheses,
# with no characters between them. No other characters will appear in the string.

eye = input() # input 
bars = eye.split('()') # list containg two strings with bars

if len(bars[0]) == len(bars[1]): # if length of both strings are equal (symmetric)
    print("correct")
else:
    print("fix")          
