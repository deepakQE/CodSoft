
while X = 'Yes': 
    a = input("Enter The Operation Performed ,'+','-','/','*','%', Type The Symbol")
b = int(input("Enter the First Digit"))
c = int(input("Enter the First Digit"))
if a =='+':
    d =b+c
    print("Your Value is ", d)
elif a =='-':
    d =b-c
    print("Your Value is ", d)
elif a =='/':
    d =b/c
    print("Your Value is ", d)
elif a =='*':
    d =b*c
    print("Your Value is ", d)
elif a =='%':
    d =b-c
    print("Your Value is ", d)
else:
         print("Something went Error Retry ")
         
         X = input("Enter 'Yes ' if Want  To More calculation and 'No' For Exit  ")
        #