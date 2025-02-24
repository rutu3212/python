
#assignment
# any story develop and craete program using elif max 30 line
print("Welcome to the Mysterious Forest Adventure!")
print("You find yourself in a dense forest. There are two paths ahead.")

choice1 = input("Do you take the 'left' path or the 'right' path? ").lower()

if choice1 == "left":
    print("You see a river blocking your way.")
    choice2 = input("Do you 'swim' across or 'build' a raft? ").lower()
    
    if choice2 == "swim":
        print("Oh no! The river is too strong. You got swept away! Game over.")
    elif choice2 == "build":
        print("You build a raft and safely cross. You find a hidden treasure! You win!")

elif choice1 == "right":
    print("You hear a growl. A wild wolf appears!")
    choice2 = input("Do you 'run' away or 'climb' a tree? ").lower()
    
    if choice2 == "run":
        print("The wolf chases you down. You didn't make it. Game over.")
    elif choice2 == "climb":
        print("You wait until the wolf leaves, then escape safely. You win!")

else:
    print("You hesitate for too long and get lost forever. Game over.")
