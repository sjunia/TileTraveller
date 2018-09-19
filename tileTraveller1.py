#Algorithm for project TileTraveller
#1. Program prints valid directions to move from current tile
#2. If player choses not valid direction program prints on screen Not valid direction!
#3. If player choses vaild move he moves to the next tile
#4. When player reaches final tile 3.1 he wins the game
#5. Program goes back to line 1 if not on final tile


current_x = 1
current_y = 1
win = False

while win is False:
    #1.1
    if current_x == 1 and current_y == 1:
        print("You can travel:  (N)orth.")
        selection = input("Direction: ")
        if selection is "n" or selection is "N":
            current_x = 1
            current_y = 2
            continue
        else: 
            while selection is not "n" or selection is not "N":
                print("Not a valid direction!")
                selection = input("Direction: ")
                if selection is "n" or selection is "N":
                    current_x = 1
                    current_y = 2
                    break
                


    #1.2 
    if current_x == 1 and current_y == 2:
        print("You can travel: (N)orth or (E)ast or (S)outh.")
        selection = input("Direction: ")
        if selection is "n" or selection is "N":
            current_x = 1
            current_y = 3
            continue
            
        elif selection is "e" or selection is "E":
            current_x = 2
            current_y = 2
            continue
            
        elif selection is "s" or selection is "S":
            current_x = 1
            current_y = 1
            continue
        else:
              while selection is not "n" or selection is not "N" or selection is not "e" or selection is not "E" or selection is not "s" or selection is not "S":
                print("Not a valid direction!")
                selection = input("Direction: ")
                if selection is "n" or selection is "N":
                    current_x = 1
                    current_y = 3
                    break
                elif selection is "e" or selection is "E":
                    current_x = 2
                    current_y = 2
                    break
            
                elif selection is "s" or selection is "S":
                    current_x = 1
                    current_y = 1
                    break

    #1.3
    if current_x == 1 and current_y == 3:
        print("You can travel: (E)ast or (S)outh")
        selection = input("Direction: ")
        if selection is "e" or selection is "E":
            current_x = 2
            current_y = 3
            continue
        if selection is "s" or selection is "S":
            current_x = 1
            current_y = 2
            continue
        else:
            while selection is not "e" or selection is not "E":
                print("Not a valid direction!")
                selection = input("Direction: ")
                if selection is not "e" or selection is not "E":
                    current_x = 2
                    current_y = 3
                    break
                if selection is not "s" or selection is not "S":
                    current_x = 1
                    current_y = 2
                    break
            

    #2.1
    if current_x == 2 and current_y == 1:
        print("You can travel: (N)orth")
        selection = input("Direction: ")
        if selection is "n" or selection is "N":
            current_x = 2
            current_y = 2
            continue
        else:
            print("Not a valid direction!")
            selection = input("Direction: ")
            	
    
    #2.2
    if current_x == 2 and current_y == 2:
        print("You can travel: (S)outh or (W)est")
        selection = input("Direction: ")
        if selection is "s" or selection is "S":
            current_x = 2
            current_y = 1
            continue
        if selection is "w" or selection is "W":
            current_x = 1
            current_y = 2
            continue
        else:
            print("Not a valid direction!")
            selection = input("Direction: ")
    #2.3
    if current_x == 2 and current_y == 3:
        print("You can travel: (E)ast or (W)est")
        selection = input("Direction: ")
        if selection is "e" or selection is "E":
            current_x=3
            current_y=3
            continue
        if selection is "w" or selection is "W":
            current_x=1
            current_y=3
            continue
        else:
            print("Not a valid direction!")
            selection = input("Direction: ")

    #3.2
    if current_x == 3 and current_y == 2:
        print("You can travel: (N)orth or (S)out")
        selection = input("Direction: ")
        if selection is "n" and selection is "N":
            current_x=3
            current_y=3
        if selection is "s" or selection is "S":
            current_x=3
            current_y=1
        else:
            print("Not a valid direction!")
            selection = input("Direction: ")
    #3.3
    if current_x == 3 and current_y == 3:
        print("You can travel: (S)outh or (W)est")
        selection = input("Direction: ")
        if selection is "s" or selection is "S":
            current_x=3
            current_y=2
            continue
        if selection is "w" or selection is "W":
            current_x=2
            current_y=3
            continue

        else:
            print("Not a valid direction!")
            selection = input("Direction: ")
    
    #3.1
    if current_x == 3 and current_y == 1:
        win = True
        break 
 

print("You won")


        






    




