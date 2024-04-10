


from random import choice
while True:
       
       
    
       a = int(input("Enter The Length of Password "))
       if a <=30:
           b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0','1','2','3','4','5','6','7','8','9','!','@','#','$','%','^','&','*','?']
    
           print("Your Password is: ")
           for i in range(a):
              c = (choice(b))
              print(c,end="") 
       else:
          print("Please Choose upto 30 Character ", a)
       print("") 
       x = input("Click 'Yes' for Regenrate & 'No' for exit the program: ") 
       if x.lower() == "yes":
          continue
       else:
          break
        




