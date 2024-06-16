import sys
from tournament import Tournament
from untested_helpers import power_of_two
from scheduler import Scheduler

def starting_menu():
    print("*************************************************************")
    print("Welcome to our tournament management tool!")
    print("You can press '1' to create a new tournament")
    print("You can press '2' to edit the games of an existing tournament")
    print("You can press any other key to exit\n")

    operation = input("What would you like to do? ")

    if operation == '1':
        tournament_setup()
    elif operation == '2':
        tournament_changes()
    else:
        print("Thanks for using our tool! exiting now...")
        sys.exit()

def tournament_setup():
    tournament_name = input("\nWhat would you like to call your tournament? ")
    tournament = Tournament(tournament_name)

    
    participant_count = request_participant_count("How many participants will enter this tournament? ")

    
    participants = request_participants(participant_count)

    print("\nYour tournament is ready to be scheduled. Creating calendar invites now!")
    
    tournament.create_games(participants)
    print(f'{tournament=}')
    tournament_scheduler = Scheduler()
    tournament_scheduler.schedule_tournament(tournament)
    tournament.save()


    starting_menu()

def tournament_changes():
    tournament_name = input("What tournament would you like to modify? ")

    try:
        tournament = Tournament.load_tournament(tournament_name)
    except:
        print("Could not find the tournament, try again!")
        starting_menu()

    if not tournament.has_games():
        print("The tournament we found has no games on record!, exiting")
        starting_menu()

    for i, game in enumerate(tournament.games):
        print(f'Press - {i} to edit {game}')

    game_id = -1
    while game_id < 0 or game_id >= len(tournament.games):
        game_id = request_integer_input("Which game do you want to modify?  ")

    player_1 = input("Please enter the new player 1, or type enter not to change it: ")
    player_2 = input("Please enter the new player 2, or type enter not to change it: ")

    print("-----------------------")
    print("Saving your changes now")
    print("-----------------------")

    tournament.update_game(game_id, player_1, player_2)

    starting_menu()



# Must return a list of UNIQUE participants equal to the count
def request_participants(count):
    participant_list = []
    while count > 0:
        participant = input('Please provide a participant: ')
        while participant in participant_list:
            participant = input('Please provide a participant: ')
        participant_list.append(participant)
        count -= 1
    return participant_list
            


# Must ask for input and only accept multiples of two
def request_participant_count(value):
    while True:
        try:
            participant_input = int(input(value))
            if power_of_two(participant_input):
                return participant_input
            else:
                print("Sorry, please make sure the number is a power of two")
        except ValueError:
            print("Sorry, please make sure to type in a number")

""" Helpers:
"""
def request_integer_input(message):
    int_input = input(message).strip()
    while not int_input.isnumeric():
        print("Sorry, please make sure to type in a number")
        int_input = input(message).strip()

    return int(int_input)

if __name__ == '__main__':
    starting_menu()
