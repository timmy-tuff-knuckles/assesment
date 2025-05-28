#assesment 2
#judah thornton
#28 may 2025
#v1

#ask for the length of fence and repate until a number above zero is entered

loop = '' #create a loop
while loop == '':
    question_legth = int(input('what it the length of the desired area to be measured in M: '))
    if question_legth>0: #do an if to make sure the number is over 0
        print (f'the length of the desired area is {question_legth}')
        question_width = int(input('what it the width of the desired area to be measured in M: '))
        
        if question_width>0:#ask for width than do a if
            print (f'the cost per meter of the desired area is {question_width}')
            cost_per_meter = int(input('what is the cost per meter in nzd: '))
            if cost_per_meter>0:
                print (f'the cost per meter of the desired area is {cost_per_meter}\n')
                awnser = (question_width+question_legth)
                print (f'this is the length for fence you will need {awnser}\n')
                awnser_2=(awnser*cost_per_meter)
                print (f'this is how much it will cost for all the fencing {awnser_2}\n')
                continue_question = (input('if you would like to continue press enter if not press enter no bellow:\n'))
                if continue_question == 'no':
                    loop = 'done :D'
            else:
                print (f'the legth of the desired area is {cost_per_meter}')
                print ('please enter a valid number obove zero')    
        else:
            print (f'the width of the desired area is {question_width}')
            print ('please enter a valid number obove zero')    
    else:
        print (f'the length of the desired area is {question_legth}')
        print ('please enter a valid number obove zero')