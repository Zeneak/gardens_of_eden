from functions.roll import roll
#main loop for Garden of Erden system

loop = True
while loop == True:
    answer = input('What would you like to do? ')
    if answer == "help" or answer == "Help":
        print("You can roll, or quit")
    elif answer == 'quit' or answer == 'Quit':
        loop = False
    elif answer == "roll" or answer == 'Roll':
        print("What are your numbers? Format (Attribute, Skill, Bonus, Target_Attribute, Target_Skill)")
        data1, data2, data3, data4, data5 = input(">").split(',')

        roll(data1, data2, data3, data4, data5)
    else:
        print('Do you need help? input help')