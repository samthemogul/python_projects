import json

from datetime import datetime, timedelta
import os

from game import Game
from untested_helpers import from_datetime_to_string, power_of_two, compute_round_name

class Tournament:
    def __init__(self, name, games = None):
        self.name = name
        self.start_date = datetime.now() + timedelta(days = 1)

        self.interval = 2 # games every other day
        self.game_duration = 1 #hours

        self.games = [] if games is None else games

    def create_games(self, participants):
        # We go over each "round" of the competition, and we create all the games in that round.
        # Knowing the round lets us name the games correctly: The last round is the finals
        # The round before last is the semi-finals

        # Initially, the number of games is equal to half the number of participants
        # Each time through the loop, we will divide this by 2, until we get to 1 game in the round
        games_in_round = len(participants) // 2

        rounds_count = 0
        while games_in_round > 0:
            round_name = compute_round_name(games_in_round)

            for game_count in range(games_in_round):
                game_name = f'{round_name} Game {game_count + 1}'
                game_start, game_end = self.compute_game_time(rounds_count)
                if rounds_count == 0:
                # The first round is special because we know all the competitors, so we should include them in the game
                    player_1 = participants[2*game_count]
                    player_2 = participants[2*game_count + 1]
                    self.games.append(Game(game_name, game_start, game_end, player_1, player_2))
                else:
                    self.games.append(Game(game_name, game_start, game_end))

            rounds_count += 1
            games_in_round  //= 2

    def __repr__(self):
        return f'{self.name} \n{self.games}'


    # Milestone 2 part 2
    def save(self):
        tournament_file = f"{self.name}.games"
        with open(tournament_file, 'w') as file:
            for game in self.games:
                file.write(game.to_json_string() + '\n')

    # Milestone 2 part 3
    @staticmethod
    def load_tournament(tournament_name):
        tournament_file = f"{tournament_name}.games"
        with open(tournament_file, 'r') as file:
            games = []
            for line in file:
                games.append(Game.from_json_string(line))
            return Tournament(tournament_name, games)

    # Milestone 3
    def update_game(self, game_id, player_1, player_2):
        self.games[game_id].update(player_1, player_2)
        self.save()

    """
    Helpers
    """
    def has_games(self):
        return len(self.games) > 0

    def compute_game_time(self, round_count):
        game_start = (self.start_date + timedelta(days = round_count * self.interval)).replace(hour = 16, minute = 0, second = 0)
        game_end = game_start + timedelta(hours = self.game_duration)

        return from_datetime_to_string(game_start), from_datetime_to_string(game_end)
