from Gamemaster import Gamemaster 


gamemaster = Gamemaster()
input_ = "Y"
while input_ == "Y" or input_ == "y":
    winner = gamemaster.game_loop()
    if winner:
        print("You Win! Congratulations!")
    else:
        print("The Enemy Won! Better Luck Next Time!")
    input_ = input("Would you like to play again? press Y for yes, N for No\n".title())
print("Thanks for Playing!")



