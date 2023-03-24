# The below line describes the goal scorers for each team. Please read the string and find how
# many times each player has scored.
# Sample input: Kane, Ronaldo, Messi, Messi, Ronaldo, Salah, Ronaldo, Mbappe, Ronaldo
# Sample output:
# Player – Ronaldo, Goal/s – 4
# Player – Messi, Goal/s – 2
# Player – Kane, Goal/s – 1
# Player – Mbappe, Goal/s – 1
# Player – Salah, Goal/s – 1

player_str = "Kane, Ronaldo, Messi, Messi, Ronaldo, Salah, Ronaldo, Mbappe, Ronaldo"

# Split the string into a list of player names
players = player_str.split(", ")

# Create an empty dictionary to store player goals
player_scored = {}

# Count the number of player name in the players array list
for player in players:
    # Check if the player is already in the dictionary
    if player in player_scored:
        # increment their score count by 1
        player_scored[player] += 1
    else:
        # If no, add them with scored 1
        player_scored[player] = 1

# Print the result for all players as seperate
for player, goals in player_scored.items():
    print(f"Player - {player}, Goal/s - {goals};")
