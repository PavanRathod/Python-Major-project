print("--------------------------")
print(" WELCOME TO TREASURE HUNT")
print("--------------------------")
print("Do you want to START the game?")

def start():
        print("\nYou are standing in a dark room.")
        print("There is a door to your left and right,which one do you take?")
        answer1=int(input("1=left & 2=right: "))
        if answer1 == 1:
             snake()
        elif answer1 == 2:
             monster_room()
        else :
             print("\nEnter a valid choice!") 
             start()             
    
def snake():
    print("\nThere is a snake here.")
    print("Behind the Snake,there is another door.")
    print("The snake is having eggs!")
    print("What would you do?")
    print("  1)Take the eggs.")
    print("  2)Taunt the snake.")
    answer2 = int(input('1 or 2: '))
    if answer2 == 1:
         game_over(1)
    elif answer2 == 2:
         treasure_room()
    else :
         print("\nEnter a valid choice")
         snake()         
     
def monster_room():
    print("\nNow you entered the room of a monster!")
    print("The monster is sleeping.\nBehind the monster, there is another door. What would you do?")
    print("  1)Go through the door silently.")
    print("  2)Kill the monster and show your courage!")
    answer3 = int(input('1 or 2: '))
    if answer3 == 1:
         treasure_room()
    elif answer3 == 2:
         game_over(2)
    else :
         print("\nEnter a valid choice")
         monster_room()         

def treasure_room():
    print("\nYou are now in a room filled with diamonds!")
    print("And there is a door too!")
    print("What would you do?(1 0r 2)")
    print("  1)Take some diamonds and go through the door.")
    print("  2)Just go through the door.")
    answer4 = int(input("1 or 2: "))
    if answer4 == 1:
         game_over(3)
    elif answer4 == 2:
         print("YAY ||| WIN")
         game_over(4)
    else :
         print("\nEnter a valid choice")
         
def game_over(reason):
    
    if reason == 1:
         print("You want eggs not the treasure !! Thats why the snake killed you.")
        
    elif reason ==2:
         print("The monster was hungry, he ate you")
         
    elif reason ==3:
         print("You are too greedy!")
       
    else:
         print("Thankyou!")
    print("Game over!")
    print("\nDo you want to play again?")
    answer5 = int(input("1=yes & 2= No: "))
    if answer5 == 1:
         start()
    else :
         print("Game Over")   
         
answer=int(input('1=Yes & 2=No:'))
if answer == 1:
     start()
elif answer == 2:
     game_over(4)
else :
     print("Enter a valid choice")
     game_over(4)     