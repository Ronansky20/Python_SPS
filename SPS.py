import random
import os
import time


def clear():
    os.system("clear")

# Set de instructies voor RPS


def rps_instructions():

    print()
    print("Instructies voor steen papier schaar : ")
    print()
    print("Steen verslaat schaar")
    print("Shcaar verslaat papier")
    print("Papier verslaat Steen")
    print()

# Set de instructies voor RPSLS


def rpsls_instructions():
    print()
    print("Intructies voor steen papier schaar lizard spock")
    print("Steen verslaat schaar")
    print("Shcaar verslaat papier")
    print("Papier verslaat Steen")
    print("Steen verslaat Lizard")
    print("Lizard vergiftigd Spock")
    print("Spock Verslaat schaar")
    print("Schaar onthoofd Lizard")
    print("Lizard eet papier")
    print("Papier weerlegt Spock")
    print("Spock verdampt Steen")
    print()


def rps():
    global rps_table
    global game_map
    global name

    # Game Loop voor elke match of Steen Papier Schaar
    while True:

        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" voor instructies")
        print("Enter \"Steen\",\"Papier\",\"Schaar\" om te spelen")
        print("Enter \"exit\" om te stoppen")
        print("--------------------------------------")

        print()

        # Player Input
        inp = input("Vul uw zet in : ")
        if inp.lower() == "help":
            clear()
            rps_instructions()
            continue
        elif inp.lower() == "exit":
            clear()
            break
        elif inp.lower() == "steen":
            player_move = 0
        elif inp.lower() == "papier":
            player_move = 1
        elif inp.lower() == "schaar":
            player_move = 3
        elif inp.lower() == "Steen":
            player_move = 0
        elif inp.lower() == "Papier":
            player_move = 1
        elif inp.lower() == "Schaar":
            player_move = 3
        else:
            clear()
            print("Verkeerde input!")
            rps_instructions()
            continue

        print("De PC is een move aan het doen.....")

        print()
        time.sleep(2)

        # Zorgt ervoor dat de PC een random move maakt
        comp_move = random.randint(0, 2)

        # Print de PC move
        print("Computer chooses ", game_map[comp_move].upper())

        # Vind de winnaar van de match
        winner = rps_table[player_move][comp_move]

        # Maakt de winnaar bekend
        if winner == player_move:
            print(name, "WINT!!!!!")
        elif winner == comp_move:
            print("COMPUTER WINT!!!")
        else:
            print("TIE GAME")
        print()
        time.sleep(2)
        clear()


def rpsls():

    global rpsls_table
    global game_map
    global name

    # Game loop voor elek match Steen papier schaar Lizard Spock
    while True:
        print("--------------------------------------")
        print("\t\tMenu")
        print("--------------------------------------")
        print("Enter \"help\" voor instructies")
        print("Enter \"Steen\",\"Papier\",\"Schaar\",\"Lizard\",\"Spock\" om te spelen")
        print("Enter \"exit\" om te stoppen")
        print("--------------------------------------")

        print()

        # Speler input
        inp = input("Vul uw zet it : ")

        if inp.lower() == "help":
            clear()
            rpsls_instructions()
            continue
        elif inp.lower() == "exit":
            clear()
            break
        elif inp.lower() == "steen":
            player_move = 0
        elif inp.lower() == "papier":
            player_move = 1
        elif inp.lower() == "schaar":
            player_move = 2
        elif inp.lower() == "lizard":
            player_move = 3
        elif inp.lower() == "spock":
            player_move = 4
        elif inp.lower() == "Steen":
            player_move = 0
        elif inp.lower() == "Papier":
            player_move = 1
        elif inp.lower() == "Schaar":
            player_move = 2
        elif inp.lower() == "Lizard":
            player_move = 3
        elif inp.lower() == "Spock":
            player_move = 4
        else:
            clear()
            print("Verkeerde Input!")
            rpsls_instructions()
            continue

        print("De PC is een move aan het doen.....")

        print()
        time.sleep(2)

        # Zorgt ervoor dat de PC een random move maakt
        comp_move = random.randint(0, 4)

        # Print de PC move
        print("Computer chooses ", game_map[comp_move].upper())

        # Vind de winnaar van de match
        winner = rps_table[player_move][comp_move]

        # Maakt de winnaar bekend
        if winner == player_move:
            print(name, "WINT!!!!!")
        elif winner == comp_move:
            print("COMPUTER WINT!!!")
        else:
            print("TIE GAME")
        print()
        time.sleep(2)
        clear()


# De Main functie
if __name__ == '__main__':
    # De mapping tussen moves en nummers
    game_map = {0: "steen", 1: "papier", 2: "schaar", 3: "lizard", 4: "Spock"}

    # Win->Verlies ratio voor steen papier schaar game
    rps_table = [[-1, 1, 0], [1, -1, 2], [0, 2, -1]]

    # Win -> Verlies Ratio voor steen papier schaar lizard spock game
    rpsls_table = [[-1, 1, 0, 0, 4], [1, -1, 2, 3, 1],
                   [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]

    name = input("Voer je naam in:")


while True:
    # De game loop
    print()
    print("Tijd om te beginnen!")
    print("Welke versie van RPS wil je spelen?")
    print("Typ 1 om Rock-Paper-scissors te spelen")
    print("Typ 2 om Rock-Paper-scissors te spelen")
    print("Typ 3 om te stoppen")
    print()

    # Try block om de spelers keuze te hanteren
    try:
        choice = int(input("Voer je keuze in = "))
    except ValueError:
        clear()
        print("Verkeerde keuze")
        continue

    # RPS deel
    if choice == 1:
        rps()

    # Speel RPSLS
    elif choice == 2:
        rpsls()

    # Stop met spelen
    elif choice == 3:
        break

    # Nog een verkeerde input
    else:
        clear()
        print("Verkeerde keuze. Lees de instructies opnieuw")
