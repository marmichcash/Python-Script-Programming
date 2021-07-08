# This program saves player names and their respective score
# in a golf tournament to the golf.txt file.

def main():
    # get the number of players in the tournament
    num_players = int(input("Enter number of players: "))

    # open golf.txt file to hold player names and scores
    golf_file = open("golf.txt", "w")

    # get each player's name and score and write it to golf.txt file
    for count in range(1, num_players + 1):
        player_name = input(f"Enter name of player number {count}: ")
        golf_file.write(f"{player_name}\n")
        player_score = float(input(f"Enter score of player number {count}: "))
        golf_file.write(f"{player_score}\n")

    # close golf.txt file
    golf_file.close()

    # let user know the data has been stored
    print("Player names and scores for Springfork Amateur Golf Club "
          + "tournament have been saved to golf.txt")

# call main function
main()
