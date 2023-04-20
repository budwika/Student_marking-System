#creating a variable to store no of outcomes
p = 0 
pmt = 0 
dnp = 0 
exc = 0 

#creating a list for values 
histogram = [p, pmt, dnp, exc]
histogram_names = ["Progress ", "Trailer  ", "Retriever", "Exclude  "]

#while True will run an infinite loop

while True:
    
#add a try except to identify the ValueError
    
    try:
        pass_marks=int(input('Please enter your credits at pass: ')) 
        if pass_marks not in range(0,121,20):
            print('Out of range')
            continue
        
        defer=int(input('Please enter your credits at defer: '))
        if defer not in range(0,121,20):
            print('Out of range')
            continue
        
        fail=int(input('Please enter your credits at fail: '))
        if fail not in range(0,121,20):
            print('Out of range')
            continue
        
#if sum doesn't match print error message
        if pass_marks+defer+fail!=120:
            print ('Total Incorrect')
            continue
       
    except(ValueError):
        print('Integer required')
        continue

#continue if sum of the inputs are equal 120 and get the progress output
    if pass_marks+defer+fail==120:
        
        if pass_marks==120 :
            p = p + 1
            print('Progress')
            
        elif pass_marks==100 :
            pmt = pmt + 1
            print('Progress (module trailer)')
            
        elif 80>=pass_marks>=0 and (120>=defer>=0 and 60>=fail>=0):
            dnp = dnp + 1
            print('Module retriever')
            
        elif 40>=pass_marks>=0 and (40>=defer>=0 and 120>=fail>=80):
            exc = exc + 1
            print('Excluded')
            
        
#loop breaks if user input "q"
    resp=(input('''Would you like to enter another set of data?
    Enter 'y' for yes or 'q' to quit and view results:'''))
    
    resp=resp.lower()
    
    if resp=="q":
        break
    if resp=="y":
        continue

#print histogram
histogram = [p, pmt, dnp, exc]
    
for i in range(len(histogram)):
    print(histogram_names[i]," ",histogram[i],':',"*"*histogram[i])
print()

#print total outcomes
print(sum(histogram),"outcomes in total.")
