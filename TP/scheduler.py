from event_brite_client import EventBriteAPIHelper

class Scheduler():
    def __init__(self):
        self.client = EventBriteAPIHelper()
    # Milestone 5:
    def schedule_tournament(self, tournament):
        # get game information from tournament and use to create eventbrite event
        games = tournament.games
        for game in games:
            game.event_id = self.client.create_event(game.name, game.description(), game.start_time, game.end_time)
        tournament.save()

    def update_game_event(self, game):
        # get game details and update them by id
        self.client.update_event(game.event_id, game.name, game.description(), game.start_time, game.end_time)
        