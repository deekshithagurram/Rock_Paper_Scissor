import random 
  
 
print("Winning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
while True:
    user_choice=int(input("UserChoice  :"))
    while user_choice>3 or user_choice<1:
        user_choice=int(input("Enter Valid Choice  "))
    if user_choice==1:
        user_choice_name="Rock"
    elif user_choice==2:
        user_choice_name="Paper"
    else:
        user_choice_name="Scissor"

    print("UserChoice is  " ,user_choice)
    print("\n")
    print("Now Computer Choice")
    comp_choice=random.randint(1,3)
    while comp_choice == user_choice: 
        comp_choice = random.randint(1, 3) 
    if comp_choice==1:
        comp_choice_name="Rock"
    elif comp_choice==2:
        comp_choice_name="Paper"
    else:
        comp_choice_name="Scissor"
    print("ComputerChoice is" ,comp_choice)
    print("UserChoice V/S ComputerChoice")
    if((user_choice==1 and comp_choice==2) or(user_choice==1 and comp_choice==2)):
        result="Paper"
    elif((user_choice==1 and comp_choice==3) or (user_choice==3 and comp_choice==1)):
        result="Rock"
    else:
        result="Scissor"
    if(result==user_choice):
        print("UserWins")
    else:
        print("ComputerWins")
    print("\n")
   
    k=input("The User Want To Play Again Y/N            :")

    if(k=="n" or k== "N"):
        break
print("Thanks For Playing")

        
    
        

    
    
          
    
  
