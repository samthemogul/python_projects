import unittest
from unittest.mock import Mock, patch
from helpers import datetime_to_eventbrite_format

from tournament import Tournament
from game import Game
from main import request_participant_count, request_participants

# class TestTournamentCLI(unittest.TestCase):
#     def test_request_participant_count(self):
#         pass

#     def test_request_participants(self):
#         pass

class TestGame(unittest.TestCase):
    # Milestone 3
    def test_game_update(self):
        test_game = Game("test", "start_time", "end_time", "unknown", "unknown")

        test_game.update("Team A", "Team B")
        assert test_game.player_1 == "Team A"
        assert test_game.player_2 == "Team B"

        test_game.update("Team C", "")
        assert test_game.player_1 == "Team C"
        assert test_game.player_2 == "Team B"

        test_game.update("", "Team D")
        assert test_game.player_1 == "Team C"
        assert test_game.player_2 == "Team D"

class TestTournament(unittest.TestCase):
    # Milestone 2
    def test_save_tournament(self):
        test_game = Game("test", "start_time", "end_time", "Team A", "Team B")
        test_game_two = Game("test", "start_time", "end_time", "unknown", "unknown")

        test_tournament = Tournament("test", [test_game, test_game_two])

        # utility mock provided by unittest to handle file opening
        with patch('builtins.open', unittest.mock.mock_open()) as mock_file:
            test_tournament.save()
            mock_file.assert_called_once_with('test.games', 'w')

            # Hacky but works, gets all the arguments to write, then looks for specific strings within
            # This is brittle because if the code under test appends the end of line characters to the json
            # before writing, this test will fail.
            # args_set = {call.args[0] for call in mock_file().write.call_args_list}

            # assert test_game.to_json_string() in args_set
            # assert test_game_two.to_json_string() in args_set
            # assert '\n' in args_set

            written_data = ''.join(call.args[0] for call in mock_file().write.call_args_list)
            expected_data = f"{test_game.to_json_string()}\n{test_game_two.to_json_string()}\n"
            assert written_data == expected_data

    # Milestone 2
    def test_load_tournament(self):
        test_game = Game("test", "start_time", "end_time", "Team A", "Team B")
        test_game_two = Game("test", "start_time", "end_time", "unknown", "unknown")

        # utility mock provided by unittest to handle file opening
        with patch('builtins.open', unittest.mock.mock_open(read_data = f'{test_game.to_json_string()}\n{test_game_two.to_json_string()}')) as mock_file:
            new_tournament = Tournament.load_tournament("test")

            mock_file.assert_called_once_with('test.games', 'r')
            assert len(new_tournament.games) == 2
            assert new_tournament.games[0].to_json_string() == test_game.to_json_string()
            assert new_tournament.games[1].to_json_string() == test_game_two.to_json_string()
    
    # Milestone 3
    def test_tournament_update(self):
        test_game = Game("test", "start_time", "end_time", "Team A", "Team B")
        test_game_two = Game("test", "start_time", "end_time", "unknown", "unknown")

        test_tournament = Tournament("test", [test_game, test_game_two])

        test_tournament.update_game(1, "", "New Player")
        assert test_game_two.player_2 == "New Player"
        assert test_game_two.player_1 == "unknown"
        assert test_game.player_1 == "Team A"
        assert test_game.player_2 == "Team B"

        with self.assertRaises(IndexError):
            test_tournament.update_game(2, "A", "B")

class TestEvenBriteClient(unittest.TestCase):

    def test_update_event(self):
        import event_brite_client

        api_key = "fake_api_key"
        with patch('builtins.open', unittest.mock.mock_open(read_data = api_key)):
            client = event_brite_client.EventBriteAPIHelper()
            # import pdb
            # pdb.set_trace()
            event_brite_client.request = Mock()
            

            event_brite_client.request.Request = Mock()
            start_time = '2033-01-01T00:00:00Z'
            end_time = '2033-12-12T00:00:00Z'

            client.update_event('some_id', 'new title', 'new description', start_time, end_time)
            event_brite_client.request.Request.assert_called_with(f'https://www.eventbriteapi.com/v3/events/some_id/?token={api_key}', method = 'POST')
            event_brite_client.request.urlopen.assert_called_once()

            expected_start_time = datetime_to_eventbrite_format(start_time)
            expected_end_time = datetime_to_eventbrite_format(end_time)
            expected_result = b'{"event": {"currency": "USD", "name": {"html": "new title"}, "description": {"html": "new description"}, "start": {"timezone": "UTC", "utc": "%s"}, "end": {"timezone": "UTC", "utc": "%s"}}}' % (expected_start_time.encode('utf-8'), expected_end_time.encode('utf-8'))
            assert event_brite_client.request.urlopen.call_args.kwargs.get('data') == expected_result


class TestScheduler(unittest.TestCase):
    def setUp(self):
        self.test_game = Game("test", "start_time", "end_time", "Team A", "Team B")
        test_game_two = Game("test", "start_time", "end_time", "unknown", "unknown")
        self.test_tournament = Tournament("test", [self.test_game, test_game_two])

    def test_schedule_tournament(self):
        import scheduler
        scheduler.EventBriteAPIHelper = Mock()

        scheduler_object = scheduler.Scheduler()
        scheduler_object.schedule_tournament(self.test_tournament)

        assert scheduler_object.client.create_event.call_count == len(self.test_tournament.games)

    def test_update_game_event(self):
        import scheduler
        scheduler.EventBriteAPIHelper = Mock()

        scheduler_object = scheduler.Scheduler()

        scheduler_object.update_game_event(self.test_game)

        scheduler_object.client.update_event.assert_called_once()

if __name__ == "__main__":
    unittest.main()
