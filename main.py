import random
import csv
from operator import itemgetter
top_Players = 5
ACCOUNT_SCORE = "C:\\Users\\psyli\\PycharmProjects\\pythonProject\\Cards_game_results.csv"
ACCOUNT_FILE = "C:\\Users\\psyli\\PycharmProjects\\pythonProject\\Card_game_detail.csv"
starting_deck = [["Red", 1], ["Red", 2], ["Red", 3], ["Red", 4], ["Red", 5], ["Red", 6], ["Red", 7], ["Red", 8],
                 ["Red", 9], ["Red", 10], ["Black", 1], ["Black", 2], ["Black", 3], ["Black", 4], ["Black", 5],
                 ["Black", 6], ["Black", 7], ["Black", 8], ["Black", 9], ["Black", 10], ["Yellow", 1], ["Yellow", 2],
                 ["Yellow", 3], ["Yellow", 4], ["Yellow", 5], ["Yellow", 6], ["Yellow", 7], ["Yellow", 8],
                 ["Yellow", 9], ["Yellow", 10]]

def before_login_welcoming_messages():
    print("\n-----------------------------------------------------------------------------")
    print("Welcome to the Card Game! To play, 2 players should either login or register!")
    print("-----------------------------------------------------------------------------\n")
    game_overview()

def game_overview():
    print(
        "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("The game is as follows:\n")
    print(
        "The game uses a deck which contains 30 cards. Each card has one colour (black, red or yellow). Each card has a number\n"
        "(1,2,3,4,5,6,7,8,9,10) for each colour and each card is unique. Before starting the game, 30 cards are shuffled and\nstored in a deck.")
    print(
        "+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

def game_rules():
    print(
        "-------------------------------------------------------------------------------------------------------------------")
    print("The rules of the game is as follows:\n")
    print(
        "Player 1 takes the top card from the deck. Player 2 then takes the next card from the deck. If both players have a\n"
        "card of the same colour, the player with the highest number wins. If both players have cards with different colours,\n"
        "the winning colour is according to the rule below.")
    print("Red wins over Black, Yellow wins over Red, Black wins over Yellow.")
    print(
        "The winner of each round keeps both cards. The players keep playing until there is no more cards left in the deck.")
    print(
        "-------------------------------------------------------------------------------------------------------------------")

def login(file, username, password):
    login_value = False
    with open(file, "r") as detailfile:
        variable = csv.reader(detailfile, delimiter=",")
        for row in variable:
            if row[0] == username and row[1] == password:
                login_value = True
                break
    detailfile.close()
    return login_value

def register(file, username, password):
    with open(file, "a", newline="") as detailfile:
        detailfile.write(str(username) + "," + str(password) + "\n")
    detailfile.close()

def password_check(password, username):
    capital_letters = False
    for x in range(len(password)):
        if password[x].isupper():
            capital_letters = True
            break
    if not capital_letters:
        print("\nYour password must include a capital letters.\n")
        return False
    if password == username:
        print("\nYour password should not be the same as your username.\n")
        return False
    if len(password) < 7 or len(password) > 20:
        print("\nYour password should be between 7 to 20 characters.\n")
        return False
    return True

def username_check(username, file):
    with open(file, "r") as detailfile:
        variable = csv.reader(detailfile, delimiter=",")
        for row in variable:
            if row[0] == username:
                detailfile.close()
                return False
        else:
            detailfile.close()
            return True

def login_register(player_id):
    choice = str(input("Player " + str(player_id) + ", please login by entering either 'yes' or 'no'?\n"))
    if choice.lower() == "yes" or choice.lower() == "y":
        username = input("\nPlayer " + str(player_id) + " please input your username.\n")
        password = input("\nPlayer " + str(player_id) + " please input your password.\n")
        status = login(ACCOUNT_FILE, username, password)
        if status:
            return [1, username]
        elif not status:
            return [0, username]

    elif choice.lower() == "no" or choice.lower() == "n":
        username = input("\nPlayer " + str(player_id) + " please input the username that you would like.\n")
        username_validation = username_check(username, ACCOUNT_FILE)
        while not username_validation:
            username = input("\nPlease input a username which doesn't already exist.\n")
            username_validation = username_check(username, ACCOUNT_FILE)
        password = input("\nPlayer " + str(player_id) + " please input a password of your choice.\n")
        password_validation = password_check(password, username)
        while not password_validation:
            password = input("Please input another password of your choice.\n")
            password_validation = password_check(password, username)
        register(ACCOUNT_FILE, username, password)
        print("\n" + username + " has successfully created an account.\n")
        return [1, username]
    else:
        return [-1, player_id]

def create_shuffled_deck(deck):
    #Shuffles the game deck
    random.shuffle(deck)
    return deck

def chose_cards1(deck, username):
    question_check = False
    question = str(input("\n" + username + " type 'yes' to pick your card or type 'end' to forfeit the game.\n"))
    while not question_check:
        if question.lower() == "yes" or question.lower() == "y":
            card11 = deck.pop()
            print("\n" + username + " chose " + str(card11))
            return card11
        elif question.lower() == "end":
            return -100
        else:
            question_check = False
            question = str(
                input("\n" + username + ", type 'yes' to pick your card or type 'end' to forfeit the game.\n"))

def chose_cards2(deck, username):
    question_check = False
    question = str(input("\n" + username + " type 'yes' to pick your card or type 'end' to forfeit the game.\n"))
    while not question_check:
        if question.lower() == "yes" or question.lower() == "y":
            card22 = deck.pop()
            print("\n" + username + " chose " + str(card22))
            return card22
        elif question.lower() == "end":
            return -100
        else:
            question_check = False
            question = str(
                input("\n" + username + ", type 'yes' to pick your card or type 'end' to forfeit the game.\n"))

def start_game(username1, username2):
    game_deck = create_shuffled_deck(starting_deck)
    round_num = 1
    player1_cards = []
    player2_cards = []
    while len(game_deck) != 0:
        print("\nRound " + str(round_num) + ":\n")
        card1 = chose_cards1(game_deck, username1)
        if card1 == -100:
            player2_cards.extend(game_deck)
            player2_cards.extend(player1_cards)
            player1_cards.clear()
            break
        card2 = chose_cards2(game_deck, username2)
        if card2 == -100:
            player1_cards.extend(game_deck)
            player1_cards.extend(player2_cards)
            player1_cards.append(card1)
            player2_cards.clear()
            break
        if card1[0] == card2[0]:
            if card1[1] > card2[1]:
                player1_cards.append(card1)
                player1_cards.append(card2)
                print("\n" + username1 + " won the round " + str(round_num))
                print("\n" + username1 + " has " + str(len(player1_cards)) + " cards.\n" + username2 + " has " + str(
                    len(player2_cards)) + " cards.")
            else:
                player2_cards.append(card1)
                player2_cards.append(card2)
                print("\n" + username2 + " won the round " + str(round_num))
                print("\n" + username1 + " has " + str(len(player1_cards)) + " cards.\n" + username2 + " has " + str(
                    len(player2_cards)) + " cards.")
        else:
            if (card1[0] == "Red" and card2[0] == "Black") or (card1[0] == "Yellow" and card2[0] == "Red") or (
                    card1[0] == "Black" and card2[0] == "Yellow"):
                player1_cards.append(card1)
                player1_cards.append(card2)
                print("\n" + username1 + " won the round " + str(round_num))
                print("\n" + username1 + " has " + str(
                    len(player1_cards)) + " cards.\n" + username2 + " has " + str(len(player2_cards)) + " cards.")
            else:
                player2_cards.append(card1)
                player2_cards.append(card2)
                print("\n" + username2 + " won the round " + str(round_num))
                print("\n" + username1 + " has " + str(
                    len(player1_cards)) + " cards.\n" + username2 + " has " + str(len(player2_cards)) + " cards.")
        round_num += 1
    player1_score = len(player1_cards)
    player2_score = len(player2_cards)
    if player1_score > player2_score:
        print("\nCongratulations " + username1 + ", you won the game!!!\n")
        print("The cards that " + username1 + " won are:\n" + str(player1_cards))
    else:
        print("\nCongratulations " + username2 + ", you won the game!!!\n")
        print("The cards that " + username2 + " won are:\n" + str(player2_cards))
    return [player1_score, player2_score]

def display_top_players(file):
    with open(file, "r") as detailfile:
        variable = csv.reader(detailfile, delimiter=",")
        next(variable, None)
        username_score = []
        for row in variable:
            username_score.append([row[0], int(row[1])])
        username_score_sorted = sorted(username_score, key=itemgetter(1), reverse=True)
        if len(username_score) < top_Players:
            print("\nYou do not have " + str(top_Players) + " players in your results list yet. Here is your top "
                                                            "players: \n")
            place1 = 1
            for x in range(len(username_score)):
                print(str(place1) + ". " + str(username_score_sorted[x][0]) + " has won " + str(
                    username_score_sorted[x][1]) + " cards in total.\n")
                place1 += 1
        else:
            print("\nTop 5 player of All Time are:\n")
            place2 = 1
            for x in range(top_Players):
                print(str(place2) + ". " + str(username_score_sorted[x][0]) + " has won " + str(
                    username_score_sorted[x][1]) + " cards in total.\n")
                place2 += 1
    detailfile.close()

def store_results(username, file, score):
    old_user = False
    with open(file, "r") as detailfile:
        reader = csv.reader(detailfile, delimiter=",")
        next(reader, None)
        old_username_score = []
        for row in reader:
            old_username_score.append([row[0], int(row[1])])
    detailfile.close()
    for row in old_username_score:
        if row[0] == username:
            row[1] = row[1] + score
            old_user = True
            break
    if not old_user:
        old_username_score.append([username, score])
    with open(file, "w", newline="") as detailfile:
        writer = csv.writer(detailfile, delimiter=",")
        writer.writerow(["Username", "Total"])
        writer.writerows(old_username_score)
    detailfile.close()

def authenticate_players():
    num_players = 0
    player_id = 0
    players = []
    same_player = False
    while num_players < 2:
        player_id += 1
        status = login_register(player_id)
        if status[0] == -1:
            print("Please enter either 'yes' or 'no'\n")
            player_id -= 1
            continue
        if status[0] == 0:
            print("\nThe username and password that has been entered doesn't match.\n")
            player_id -= 1
            continue
        if len(players) > 0:
            for username in players:
                if status[1] == username:
                    same_player = True
        if status[0] == 1:
            if same_player:
                print("\nTwo players with the same username cannot play this game!")
                player_id -= 1
                same_player = False
                continue
            else:
                print("\n" + status[1] + " has successfully signed into his/her account.")
                print(status[1] + " is ready to play!\n")
                num_players += 1
                players.append(status[1])
    return players

def game_open():
    before_login_welcoming_messages()
    players = authenticate_players()
    game_rules()
    player1_username = players[0]
    player2_username = players[1]
    scores = start_game(player1_username, player2_username)
    player1_score = scores[0]
    player2_score = scores[1]
    store_results(player1_username, ACCOUNT_SCORE, player1_score)
    store_results(player2_username, ACCOUNT_SCORE, player2_score)
    display_top_players(ACCOUNT_SCORE)

game_open()
