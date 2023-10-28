# write a program that calculates a person's bmi based off of height and weight
#bmi=weight(kg)/height^2(m^2)
#bmi to be printed out as a whole number

# 1st input: enter height in meters e.g:1.65
height=input()
#2nd input: enter weight in kilograms e.g:72
weight= input()
# dont change the code above

#write your code below this line
bmi= int(weight)/float(height)**2

print(int(bmi))