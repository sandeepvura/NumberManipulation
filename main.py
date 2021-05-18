# ## Division 
# print(3/2 ) # output = 1.5

# ##If you want to round of the output of floating value to Int -- Floored division method
# print(3//2) # output = 1

# ###Other way instead floored Division method, we can use round() function
# print(round(3/2))

# # Arthematic operators 
# score = 1
# score += 1 # This is adding the value of score (1+1)
# print(score)

# F- Strings
score = 2   # Int 
height = 1.8 # Float
isWinning = True # Boolean

#result = print("your winning is: " + score + height + isWinning)

## We cannot concatenate String with Int In previous excerises we converted the string value to Int and Int to String , Float to String , Float to Int etc..

#Here we can use "F-String" method instead of type() method to convert the variables. 

result = print(f"your score is {score}, your height is {height}, your winning is {isWinning}")