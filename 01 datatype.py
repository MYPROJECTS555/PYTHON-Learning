BOY_NAME = input("Boy-Name ")
                                         # Boy-Name will be displayed out put session, user need to give the values
BOY_AGE = float(input("B-AGE "))
                                          # B-AGE will be displayed in out pull session. Use float to convert string to float convertion .otherwise it will give error
GIRL_NAME = input("Girl-Name ")
                                          # GIRL_AGE will be displayed out put session, user need to give the values          
GIRL_AGE = float(input("G-AGE "))

age_diff  = abs(BOY_AGE - GIRL_AGE)        #abs means it will give the exact value for example boy age is 20 and girl age is 22 . itgive the result in -2 . so we use abs for absolute output. 
                                           #basically Boy_age and Girl_age is string . Inside that we will store the vlaue it may be float or int . that's why we are converting string to float.

# print (BOY_NAME + "Loves" + GIRL_NAME + "difference :" + float(age_diff) )     #concatination operator

## we have use either concatination operator OR formated string

print (f"{BOY_NAME} loves {GIRL_NAME} :age difference {age_diff}")         #  formated string 
