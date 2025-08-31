import sys, random

def get_player_move():
    while True:
        move = input("(r)ock (p)aper (s)cissors or (q)uit. Enter your move: ").lower()
        if move == 'q':
            sys.exit()
        if move in ('r', 'p', 's'):
            return move
        print("\nInvalid input. Try again.\n")

score = {"wins": 0, "losses": 0, "ties": 0}

while True:
    print(f"{score['wins']} Wins, {score['losses']} Losses, {score['ties']} Ties\n")
    player_move = get_player_move()

    moves = {'r': 0, 'p': 1, 's': 2}
    reverse_moves = {0: 'ROCK', 1: 'PAPER', 2: 'SCISSORS'}

    player = moves[player_move]
    computer = random.randint(0, 2)

    print(f"\n{reverse_moves[player]} versus {reverse_moves[computer]}", end=' ')

    result = (player - computer) % 3

    if result == 0:
        print("It's a tie!")
        score['ties'] += 1
    elif result == 1:
        print("You win!")
        score['wins'] += 1
    else:
        print("You lose!")
        score['losses'] += 1

