#fence cost calculator
#judah thornton
#28 may 2025
#v1

#ask for the length of fence and repate until a number above zero is entered

loop = '' #create a loop
while loop == '':
    try:
        question_legth = int(input('What it the length of the desired area to be measured in meters? '))

        if question_legth>0: #do an if to make sure the number is over 0
            print (f'You entered that the length of the desired area is {question_legth}.')
            question_width = int(input('What it the width of the desired area to be measured in meters? '))
            

            if question_width>0:#ask for width than do a if
                print (f'You entered that the width of the desired area is {question_width}.')
                cost_per_meter = int(input('What is the cost per meter in nzd? $'))

                if cost_per_meter>0:
                    # print (f'The cost per meter of the desired area is ${cost_per_meter}\n')
                    awnser_fence_length = ((question_width * 2)+(question_legth *2)) #put in then print the awnser 
                    print (f'This is the length for fence you will need {awnser_fence_length}.\n')
                    awnser_cost=(awnser_fence_length*cost_per_meter)#this will caulculate the cost then print your cost awnser 
                    print (f'The total cost of the fencing will be: ${awnser_cost}.\n')
                    loop = (input('if you would like to continue press <enter> or anything else to quit:\n')) #ask if they would like to finish or continue
                    
                        
                else:#this will get a number above zero 
                    print (f'the length of the desired area is {cost_per_meter}.')
                    print ('please enter a valid number above zero.')  

            else:#this will get a number above zero
                print (f'the width of the desired area is {question_width}.')
                print ('please enter a valid number above zero.')    
        
        else:#this will get a number above zero
            print (f'the length of the desired area is {question_legth}.')
            print ('please enter a valid number above zero.')
    except ValueError:
        print('please enter a valid number above zero.')

    




