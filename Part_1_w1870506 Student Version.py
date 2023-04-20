print(".....Progression Outcome Report.....")
print()

#add a try except to identify the ValueError
    
try:
    pass_marks=int(input('Please enter your credits at pass: ')) 
    if pass_marks not in range(0,121,20):
        print('Out of range')
    
    defer=int(input('Please enter your credits at defer: '))
    if defer not in range(0,121,20):
        print('Out of range')
    
    fail=int(input('Please enter your credits at fail: '))
    if fail not in range(0,121,20):
        print('Out of range')
    
    #if sum doesn't match print error message
    if pass_marks+defer+fail!=120:
        print ('Total Incorrect')
   
except(ValueError):
    print('Integer required')

#continue if sum of the inputs are equal 120 and get the progress output
if pass_marks+defer+fail==120:
    
    if pass_marks==120 :
        print('Progress')
        
    elif pass_marks==100 :
        print('Progress (module trailer)')
        
    elif 80>=pass_marks>=0 and (120>=defer>=0 and 60>=fail>=0):
        print('Module retriever')
        
    elif 40>=pass_marks>=0 and (40>=defer>=0 and 120>=fail>=80):
        print('Excluded')
            
        
