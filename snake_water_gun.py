# Create metrics for desired outputs
'''
Player                Computer
          Snake(0)   Water(1)    Gun(2)
Snake 0      D         W          L
Water 1      L         D          W
Gun   2      W         L          D

'''
import random
def greet(fx):
    # def mfx(*args, **kwargs):
    print("Good Evening")
    fx()
    print("Thanks for Using this Function")
    # return mfx

@greet
def snake_water_gun():
    while True:
        choice = input("Hit Enter to start the Game! (Press Any key & Hit enter to Quit): ")
        lst = [['D', 'W', 'L'], ['L', 'D', 'W'], ['W', 'L', 'D']]
        if len(choice) >= 1:
            print("Thanks for Playing the Game")
            break
        try:
            User_turn = int(input("Press '0' for Snake, '1' for Water & '2' for Gun & Hit Enter: "))
        except:
            print("Wrong Input, Game Terminated...")

        # Brute Force
        if User_turn == 0 or User_turn == 1 or User_turn == 2:
            comp_choice = [0, 1, 2]
            Comp_turn = random.choice(comp_choice)
            print("Computer Choice: ", Comp_turn)
            '''
            if User_turn == Comp_turn:
                print("This was a Draw...")
            elif User_turn == 0 & Comp_turn == 2 or User_turn == 1 & Comp_turn == 0 or User_turn == 2 & Comp_turn == 1:
                print("Computer Won...Try Again...")
            else:
                print("Hurrey... You Won...")'''

            if lst[User_turn][Comp_turn] == 'W':
                print("Hurrey... You Won...")
            elif lst[User_turn][Comp_turn] == 'L':
                print("Computer Won...Try Again...")
            else:
                print("This was a Draw...")


if __name__ == '__main__':
    snake_water_gun()
