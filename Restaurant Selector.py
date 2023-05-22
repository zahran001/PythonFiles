#The program provides the options of restaurants available as per user's dietary restrictions.

#Take the inputs:
# input validation is required
vegetarian = input('Is anyone in your party a vegetarian? (Yes/No)')
vegetarian = vegetarian.lower()
#Thinking about which input values are not allowed
#In the two situations given below, accurate input has to be given again:
while vegetarian != 'yes' and vegetarian != 'no':
    vegetarian = input('Invalid entry.Re-enter a choice:')

vegan = input('Is anyone in your party a vegan? (Yes/No)')
vegan = vegan.lower()
#response is converted into lowercase for my convenience

while vegan != 'yes' and vegan != 'no':
    vegan = input('Invalid entry.Re-enter a choice:')

gluten_free = input('Is anyone in your party a gluten free? (Yes/No)')
gluten_free = gluten_free.lower()

while gluten_free != 'yes' and gluten_free != 'no':
    gluten_free = input('Invalid entry.Re-enter a choice:')
#Now I have the yes or no input for every category

#Conditions
# Fleming’s Prime Steakhouse – Vegetarian: No, Vegan: No, Gluten-Free: No
# Gourmet Pizza Company – Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
# Bella’s Italian Restaurant – Vegetarian: Yes, Vegan: No, Gluten-Free: No
# True Food Kitchen – Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

#If the input for a category is yes, I will have to make sure to fulfill that requirement.
#That is, if I have someone saying he is vegetarian, I must get a vegetarian place for him.
print('Here are your restaurant choices:')

if vegetarian == 'yes':
    option1 = 'Bella\'s Italian Restaurant\nGourmet Pizza Company\nTrue Food Kitchen'
    print(option1)
# \' is a common escape sequence
if vegan == 'yes':
    option2 = 'True Food Kitchen'
    print(option2)
if gluten_free == 'yes':
    option3 = 'Gourmet Pizza Company\nTrue Food Kitchen'
    print(option3)


