# this program asks the user for the number of male and female
# students registered in a class and then displays the
# percentage of males and females
str_male = input('Enter number of male students: ') # input for number of students that are male/female
str_female = input('Enter number of female students: ') 
int_male = int(str_male) # convert string to integer
int_female = int(str_female) 
total = int_male + int_female # get total number of students
percent_male = int_male / total # get percent of students that are male/female
percent_female = int_female / total
print (f'Percent male: {percent_male:.0%}') # output student gender percentages
print (f'Percent female: {percent_female:.0%}') 
 
